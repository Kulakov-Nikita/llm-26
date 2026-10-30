import re
import hashlib
import json
import shutil

import numpy as np

from io_utils import load_json, read_jsonl, save_json, write_jsonl, file_sha256
from config import ROOT
from embeddings import tokenizer, embedder


def make_chunks(pages, config):
    tok = tokenizer(config["embedding_model"])
    chunks = []
    for page in pages:
        text = page["text"].strip()
        if not text:
            continue
        header = (f"{page['section_id']} {page['section_title']} | PDF page {page['source_pdf_page']}\n"
                  if config["include_headers"] else "")
        limit = int(config["chunk_size"]) - len(tok.encode(header, add_special_tokens=False))
        if limit <= int(config["overlap"]):
            raise ValueError("Заголовок и overlap слишком велики для выбранного chunk_size")
        spans = tok(text, add_special_tokens=False, return_offsets_mapping=True)["offset_mapping"]
        start = 0
        while start < len(spans):
            end = min(start + limit, len(spans))
            if end < len(spans):
                left = spans[start + int((end - start) * 0.65)][0]
                right = spans[end - 1][1]
                separators = ["\n\n"] if config["strategy"] == "markdown" else ["\n\n", "\n", ". "]
                for separator in separators:
                    cut = text.rfind(separator, left, right)
                    if cut >= 0:
                        end = max(start + 1, next((i for i in range(end, start, -1)
                                                   if spans[i - 1][1] <= cut + len(separator)), end))
                        break
            body = header + text[spans[start][0]:spans[end - 1][1]].strip()
            while len(tok.encode(body, add_special_tokens=False)) > int(config["chunk_size"]) and end > start + 1:
                end -= 1
                body = header + text[spans[start][0]:spans[end - 1][1]].strip()
            chunk_id = hashlib.sha256(f"{page['source_pdf_page']}:{start}:{body}".encode()).hexdigest()[:24]
            chunks.append({
                "chunk_id": chunk_id, "document_id": page["document_id"],
                "section_id": page["section_id"], "section_title": page["section_title"],
                "pdf_page": page["source_pdf_page"], "source_url": config["source_url"],
                "token_count": len(tok.encode(body, add_special_tokens=False)), "text": body,
            })
            if end == len(spans):
                break
            start = max(start + 1, end - int(config["overlap"]))
    return chunks


def index_path(config, fresh=False):
    key = {
        "sha": file_sha256(config["source"]),
        "chunking": [config[k] for k in ("strategy", "chunk_size", "overlap", "include_headers")],
        "embedding": config["embedding_model"], "pages": config["pages"], "schema": 3,
    }
    parent = ROOT / "data/indices"
    parent.mkdir(parents=True, exist_ok=True)
    digest = hashlib.sha256(json.dumps(key, sort_keys=True).encode()).hexdigest()[:12]
    current = parent / digest
    if fresh or current.exists():
        return current
    # Reuse compatible indices produced by the earlier project layout.
    metadata_path = ROOT / "data/parsed/metadata.json"
    if metadata_path.exists() and load_json(metadata_path).get("parser_version", 2) == 2:
        for manifest_path in sorted(parent.glob("*/manifest.json")):
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            old_chunking = manifest.get("config", {}).get("chunking", manifest.get("chunking", {}))
            project = manifest.get("config", {}).get("project", {})
            if (manifest.get("document_sha256") == key["sha"]
                    and project.get("pdf_page_start", config["pages"][0]) == config["pages"][0]
                    and project.get("pdf_page_end", config["pages"][1]) == config["pages"][1]
                    and old_chunking.get("strategy") == config["strategy"]
                    and old_chunking.get("chunk_size") == config["chunk_size"]
                    and old_chunking.get("overlap") == config["overlap"]
                    and old_chunking.get("include_headers") == config["include_headers"]
                    and manifest.get("embedding_model") == config["embedding_model"]):
                return manifest_path.parent
    return current


def parse_documents(config):
    import pymupdf
    
    source = ROOT / config["source"]
    section_map = load_json("data/parsed/section_map.json")
    pages, markdown = [], []
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
            text = re.sub(r"(?<=\w)-\n(?=\w)", "", text).strip()
            markdown.append(f"# OpenIntro Statistics, 4th edition\n\n## {section_id} — {title}\n\n### PDF page {number}\n\n{text}")
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
    (ROOT / "data/parsed/document.md").write_text("\n\n---\n\n".join(markdown), encoding="utf-8")
    save_json("data/parsed/metadata.json", {
        "document_id": config["document_id"], "pdf_sha256": file_sha256(config["source"]),
        "page_range": [first, last], "selected_pdf_pages": len(pages),
        "nonempty_pages": nonempty, "source_url": config["source_url"],
        "parser": "PyMuPDF page-structured", "parser_version": 3,
    })
    return nonempty


def build_index(config, rebuild=False):
    metadata_path = ROOT / "data/parsed/metadata.json"
    if (not metadata_path.exists()
            or load_json(metadata_path).get("pdf_sha256") != file_sha256(config["source"])
            or load_json(metadata_path).get("page_range") != config["pages"]):
        parse_documents(config)
    directory = index_path(config, fresh=rebuild)
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
            "document_sha256": file_sha256(config["source"]),
            "chunking": {key: config[key] for key in ("strategy", "chunk_size", "overlap", "include_headers")},
            "embedding_model": config["embedding_model"], "pages": config["pages"],
            "chunk_count": len(chunks), "vectors_shape": list(vectors.shape),
        })
    return directory