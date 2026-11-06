import re
import hashlib
import json
import shutil
import unicodedata

import numpy as np
from langchain_text_splitters import RecursiveCharacterTextSplitter, MarkdownHeaderTextSplitter

from io_utils import load_json, read_jsonl, save_json, write_jsonl, file_sha256
from config import ROOT
from embeddings import tokenizer, embedder


def _heading_key(value):
    """Normalize a section heading independently of case, spacing and PDF ligatures."""
    return " ".join(re.findall(r"[a-z0-9]+", unicodedata.normalize("NFKC", value).casefold()))


def _is_section_heading(line, section_id, section_title, page_number):
    # A running header can have the physical page number before or after its title:
    # "5.3. HYPOTHESIS TESTING FOR A PROPORTION 189".
    tokens = _heading_key(line).split()
    page = str(page_number)
    if tokens and tokens[0] == page:
        tokens.pop(0)
    if tokens and tokens[-1] == page:
        tokens.pop()
    normalized = " ".join(tokens)
    title = _heading_key(section_title)
    number = _heading_key(section_id)
    return bool(title and normalized in (title, f"{number} {title}"))


def _clean_page_text(text, section_id, section_title, page_number, headings=()):
    """Remove PDF section/running headers, but keep meaningful subsection titles.

    Match full headings even when PyMuPDF extracts them across 2–3 lines.
    Only standalone heading lines are removed, never a phrase in body prose.
    """
    lines = text.splitlines()
    nonempty = [(i, line.strip()) for i, line in enumerate(lines) if line.strip()]
    all_headings = list(dict.fromkeys([(section_id, section_title), *headings]))
    removed = set()

    for i, (line_index, line) in enumerate(nonempty):
        # Remove full main-section headings, including split headings and running
        # section headers with a page number, anywhere in the PDF page text.
        for width in (3, 2, 1):
            group = nonempty[i:i + width]
            if len(group) != width:
                continue
            candidate = " ".join(part for _, part in group)
            if any(_is_section_heading(candidate, sid, title, page_number)
                   for sid, title in all_headings):
                removed.update(idx for idx, _ in group)
                break

        # Page number and "CHAPTER ..." in the running header occur at the edges.
        near_edge = i < 3 or i >= len(nonempty) - 3
        if near_edge and (line == str(page_number)
                or re.fullmatch(rf"(?:{page_number}\s+)?CHAPTER\s+\d+(?:\.\s*|\s+).*(?:\s+{page_number})?", line, re.I)):
            removed.add(line_index)

        # Do not allow Markdown page headings from previously processed data
        # to leak into the content sent to a LangChain splitter.
        if re.fullmatch(r"(?:#{1,6}\s*)?PDF\s+page\s+\d+", line, re.I):
            removed.add(line_index)
        if re.fullmatch(r"#{1,6}\s*OpenIntro Statistics(?:,?\s*4th edition)?", line, re.I):
            removed.add(line_index)

    cleaned = "\n".join(line.rstrip() for i, line in enumerate(lines) if i not in removed)
    return re.sub(r"\n{3,}", "\n\n", cleaned).strip()


def make_chunks(pages, config):
    tok = tokenizer(config.get("llm_tokenizer", "Qwen/Qwen3-4B-Instruct-2507"))
    count = lambda text: len(tok.encode(text, add_special_tokens=False))
    chunks = []
    chunk_size = int(config["chunk_size"])
    overlap = int(config["overlap"])
    # Input pages are cleaned at parse time; clean again for callers providing
    # already saved/legacy pages.jsonl rows.
    section_headings = list(dict.fromkeys(
        (row["section_id"], row["section_title"]) for row in pages
    ))

    for page in pages:
        section_id = page["section_id"]
        section_title = page["section_title"]
        page_number = int(page["source_pdf_page"])
        text = _clean_page_text(page["text"], section_id, section_title, page_number, section_headings)
        if not text:
            continue

        # Section heading is injected exactly once into every chunk. The matching
        # heading extracted from the PDF is removed above to avoid duplication.
        header = f"{section_id} — {section_title}\n" if config["include_headers"] else ""
        reserve = count(header) + (4 if header else 0)
        size = chunk_size - reserve
        if size <= overlap:
            raise ValueError("Заголовок и overlap слишком велики для выбранного chunk_size")

        splitter = RecursiveCharacterTextSplitter(
            chunk_size=size, chunk_overlap=overlap, length_function=count
        )
        if config["strategy"] == "markdown":
            markdown = f"## {section_id} — {section_title}\n\n### PDF page {page_number}\n\n{text}"
            documents = MarkdownHeaderTextSplitter(
                headers_to_split_on=[("##", "section"), ("###", "pdf_page")],
                strip_headers=True,
            ).split_text(markdown)
            parts = [part for document in documents for part in splitter.split_text(document.page_content)]
        else:
            parts = splitter.split_text(text)

        for i, part in enumerate(parts):
            body = header + part
            token_count = count(body)
            if token_count > chunk_size:
                raise ValueError(
                    f"Размер чанка {token_count} превышает chunk_size={chunk_size} "
                    f"(страница PDF {page_number})"
                )
            chunk_id = hashlib.sha256(f"{page_number}:{i}:{body}".encode()).hexdigest()[:24]
            chunks.append({
                "chunk_id": chunk_id, "document_id": page["document_id"],
                "section_id": section_id, "section_title": section_title,
                "pdf_page": page_number, "source_file": page.get("source_file", config["source"]),
                "source_url": page.get("source_url", config["source_url"]),
                "publication_year": page.get("publication_year"),
                "token_count": token_count, "text": body,
            })
    return chunks


def index_path(config):
    key = {
        "sha": file_sha256(config["source"]),
        "document_id": config["document_id"],
        "source_url": config["source_url"],
        "chunking": [config[k] for k in ("strategy", "chunk_size", "overlap", "include_headers")],
        "embedding": config["embedding_model"],
        "chunk_tokenizer": config.get("llm_tokenizer", "Qwen/Qwen3-4B-Instruct-2507"),
        "pages": config["pages"], "schema": 7,
    }
    parent = ROOT / "data/indices"
    parent.mkdir(parents=True, exist_ok=True)
    digest = hashlib.sha256(json.dumps(key, sort_keys=True).encode()).hexdigest()[:12]
    return parent / digest


def parse_documents(config):
    import pymupdf

    source = ROOT / config["source"]
    section_map = load_json("data/parsed/section_map.json")
    pages, markdown = [], ["# OpenIntro Statistics, 4th edition"]
    section_headings = [(item["section_id"], item["title"]) for item in section_map]
    previous_section = None
    with pymupdf.open(source) as pdf:
        first, last = map(int, config["pages"])
        if first < 1 or last > len(pdf) or last - first + 1 < int(config["min_pages"]):
            raise ValueError("Диапазон должен содержать минимум 50 существующих PDF-страниц")
        for number in range(first, last + 1):
            section = next((item for item in reversed(section_map)
                            if item.get("pdf_page") and item["pdf_page"] <= number), None)
            section_id = section["section_id"] if section else "unassigned"
            title = section["title"] if section else "Unknown section"
            text = pdf[number - 1].get_text(sort=True).replace("\u00ad", "")
            text = re.sub(r"(?<=\w)-\n(?=\w)", "", text)
            text = _clean_page_text(text, section_id, title, number, section_headings)
            if section_id != previous_section:
                markdown.append(f"## {section_id} — {title}")
                previous_section = section_id
            markdown.append(f"### PDF page {number}\n\n{text}")
            pages.append({
                "document_id": config["document_id"], "source_file": config["source"],
                "source_url": config["source_url"], "publication_year": 2019,
                "source_pdf_page": number, "section_id": section_id,
                "section_title": title, "text": text,
            })
    nonempty = sum(bool(page["text"]) for page in pages)
    if nonempty < int(config["min_pages"]):
        raise ValueError(f"Извлечено только {nonempty} непустых страниц")
    write_jsonl("data/parsed/pages.jsonl", pages)
    (ROOT / "data/parsed/document.md").write_text("\n\n".join(markdown), encoding="utf-8")
    save_json("data/parsed/metadata.json", {
        "document_id": config["document_id"], "pdf_sha256": file_sha256(config["source"]),
        "page_range": [first, last], "selected_pdf_pages": len(pages),
        "nonempty_pages": nonempty, "source_url": config["source_url"],
        "parser": "PyMuPDF page-structured", "parser_version": 6,
    })
    return nonempty


def build_index(config, rebuild=False):
    metadata_path = ROOT / "data/parsed/metadata.json"
    metadata = load_json(metadata_path) if metadata_path.exists() else {}
    if (metadata.get("parser_version") != 6
            or metadata.get("pdf_sha256") != file_sha256(config["source"])
            or metadata.get("page_range") != config["pages"]):
        parse_documents(config)
    directory = index_path(config)
    if rebuild and directory.exists():
        shutil.rmtree(directory)
    directory.mkdir(parents=True, exist_ok=True)
    chunks_path, vectors_path = directory / "chunks.jsonl", directory / "vectors.npy"
    relative = directory.relative_to(ROOT)
    if not chunks_path.exists():
        write_jsonl(relative / "chunks.jsonl", make_chunks(read_jsonl("data/parsed/pages.jsonl"), config))
    chunks = read_jsonl(relative / "chunks.jsonl")
    if not vectors_path.exists():
        vectors = embedder(config["embedding_model"], config["device"]).encode(
            [row["text"] for row in chunks], batch_size=int(config["embedding_batch_size"]),
            normalize_embeddings=True, convert_to_numpy=True, show_progress_bar=True)
        np.save(vectors_path, np.asarray(vectors, dtype="float32"))
    vectors = np.load(vectors_path, mmap_mode="r")
    if len(vectors) != len(chunks):
        raise ValueError("Количество чанков не совпадает с количеством эмбеддингов")
    manifest_path = directory / "manifest.json"
    if not manifest_path.exists():
        save_json(relative / "manifest.json", {
            "document_id": config["document_id"], "source_url": config["source_url"],
            "document_sha256": file_sha256(config["source"]), "parser_version": 6,
            "chunking": {key: config[key] for key in ("strategy", "chunk_size", "overlap", "include_headers")},
            "embedding_model": config["embedding_model"],
            "chunk_tokenizer": config.get("llm_tokenizer", "Qwen/Qwen3-4B-Instruct-2507"),
            "pages": config["pages"],
            "chunk_count": len(chunks), "vectors_shape": list(vectors.shape),
            "splitter_engine": "langchain-text-splitters", "schema": 7,
        })
    return directory