import os
import re
import time
from config import ROOT
from retriever import get_retriever


def answer(question, config, k=None, mode=None, generate=True):
    k = int(config["top_k"] if k is None else k)
    if not question.strip() or not 1 <= k <= 20:
        raise ValueError("Нужен непустой вопрос и 1 <= top_k <= 20")
    start = time.perf_counter()
    hits = get_retriever(config).search(question, k, mode or config["mode"])
    retrieval_ms = round((time.perf_counter() - start) * 1000, 2)
    if not generate:
        return {"question": question, "hits": hits, "retrieval_ms": retrieval_ms}

    selected, budget, page_counts = [], int(config["max_context_tokens"]), {}
    for row in hits:
        page = row["pdf_page"]
        cost = int(row.get("token_count", len(row["text"]) // 3)) + 50
        if cost > budget or page_counts.get(page, 0) >= 2:
            continue
        selected.append(row)
        budget -= cost
        page_counts[page] = page_counts.get(page, 0) + 1
    if not selected:
        return {"answer": "Недостаточно данных в документах.", "citations": [], "retrieval_ms": retrieval_ms}

    sources = {f"S{i}": row for i, row in enumerate(selected, 1)}
    context = "\n\n".join(
        f"[{sid}] Раздел {row['section_id']}, PDF с. {row['pdf_page']}\n<source>\n{row['text']}\n</source>"
        for sid, row in sources.items())
    from openai import OpenAI
    api = OpenAI(base_url=os.getenv("OLLAMA_URL", config["llm_url"]), api_key="ollama",
                 timeout=int(config["llm_timeout"]))
    prompt_path = ROOT / config["system_prompt"]
    system_prompt = prompt_path.read_text(encoding="utf-8")
    completion = api.chat.completions.create(
        model=os.getenv("OLLAMA_MODEL", config["llm_model"]),
        temperature=float(config["llm_temperature"]), max_tokens=int(config["llm_max_tokens"]),
        messages=[{"role": "system", "content": system_prompt},
                  {"role": "user", "content": f"Вопрос: {question}\n\nИсточники:\n{context}"}],
    )
    text = completion.choices[0].message.content or ""
    used = list(dict.fromkeys(re.findall(r"\[(S\d+)\]", text)))
    invalid = [ref for ref in used if ref not in sources]
    for ref in invalid:
        text = text.replace(f"[{ref}]", "[некорректная ссылка]")
    citations = [{
        "id": ref, "source": "OpenIntro Statistics, 4th ed.",
        "section": sources[ref]["section_id"], "pdf_page": sources[ref]["pdf_page"],
        "snippet": sources[ref]["text"][:250], "score": sources[ref]["score"],
        "source_url": sources[ref].get("source_url", config["source_url"]),
    } for ref in used if ref in sources]
    usage = completion.usage
    return {
        "answer": text, "citations": citations, "invalid_citations": invalid,
        "warning": "Ответ без подтверждённых цитат" if not citations else None,
        "retrieval_ms": retrieval_ms, "total_ms": round((time.perf_counter() - start) * 1000, 2),
        "input_tokens": usage.prompt_tokens if usage else None,
        "output_tokens": usage.completion_tokens if usage else None,
    }
