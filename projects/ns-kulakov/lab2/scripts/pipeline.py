import os
import re
import time

from config import ROOT
from retriever import get_retriever


def answer(question, config, k=None, mode=None, generate=True):
    k = int(config["top_k"] if k is None else k)
    if not isinstance(question, str) or not question.strip() or not 1 <= k <= 20:
        raise ValueError("Нужен непустой вопрос и 1 <= top_k <= 20")
    question = question.strip()
    start = time.perf_counter()

    if not generate:
        hits = get_retriever(config).search(question, k, mode or config["mode"])
        return {"question": question, "hits": hits,
                "retrieval_ms": round((time.perf_counter() - start) * 1000, 2)}

    # The LLM and the embedding model use different tokenizers.
    # Count the *whole* chat prompt using Qwen's chat template, not BGE-M3 chunk lengths.
    from embeddings import tokenizer
    model_id = config.get("llm_tokenizer", "Qwen/Qwen3-4B-Instruct-2507")
    try:
        tok = tokenizer(model_id)
    except Exception as exc:
        raise RuntimeError(f"Не удалось загрузить токенизатор LLM {model_id}. "
                           "Проверьте подключение к Hugging Face или локальный кеш.") from exc

    system_prompt = (ROOT / config["system_prompt"]).read_text(encoding="utf-8")
    window = int(config.get("llm_context_window", 4096))
    output_limit = int(config["llm_max_tokens"])
    reserve = int(config.get("llm_context_reserve_tokens", 256))
    source_limit = int(config["max_context_tokens"])
    if min(window, output_limit, source_limit) < 1 or reserve < 0:
        raise ValueError("Некорректные настройки окна контекста LLM")

    def messages_for(context):
        return [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": f"Вопрос: {question}\n\nИсточники:\n{context}"},
        ]

    def prompt_tokens(messages):
        return len(tok.apply_chat_template(messages, tokenize=True, add_generation_prompt=True))

    def safe_result(message, warning, input_count, retrieval_ms=0.0):
        return {
            "answer": message, "citations": [], "invalid_citations": [],
            "warning": warning, "retrieval_ms": retrieval_ms,
            "total_ms": round((time.perf_counter() - start) * 1000, 2),
            "input_tokens": None, "output_tokens": 0,
            "estimated_input_tokens": input_count, "context_window_tokens": window,
        }

    base_tokens = prompt_tokens(messages_for(""))
    # Check the user's question before performing potentially expensive retrieval.
    if base_tokens + output_limit + reserve > window:
        return safe_result(
            "Вопрос слишком длинный для контекстного окна модели. Сократите вопрос или увеличьте окно Ollama.",
            "context_window_exceeded", base_tokens,
        )

    retrieval_start = time.perf_counter()
    hits = get_retriever(config).search(question, k, mode or config["mode"])
    retrieval_ms = round((time.perf_counter() - retrieval_start) * 1000, 2)

    selected, context, page_counts = [], "", {}
    input_count = base_tokens
    for row in hits:
        page = row["pdf_page"]
        if page_counts.get(page, 0) >= 2:
            continue
        sid = f"S{len(selected) + 1}"
        fragment = f"[{sid}]\n<source>\n{row['text']}\n</source>"
        candidate = f"{context}\n\n{fragment}" if context else fragment
        candidate_count = prompt_tokens(messages_for(candidate))
        # Both constraints use Qwen token counts including chat formatting and labels.
        if candidate_count - base_tokens > source_limit:
            continue
        if candidate_count + output_limit + reserve > window:
            continue
        selected.append(row)
        context, input_count = candidate, candidate_count
        page_counts[page] = page_counts.get(page, 0) + 1

    if not selected:
        if not hits:
            return safe_result("Недостаточно данных в документах.",
                               "no_retrieval_results", base_tokens, retrieval_ms)
        return safe_result(
            "Найденные фрагменты не помещаются в контекстное окно модели. "
            "Сократите вопрос или увеличьте окно контекста Ollama.",
            "context_window_exceeded", base_tokens, retrieval_ms,
        )

    sources = {f"S{i}": row for i, row in enumerate(selected, 1)}
    messages = messages_for(context)
    from openai import OpenAI
    api = OpenAI(base_url=os.getenv("OLLAMA_URL", config["llm_url"]), api_key="ollama",
                 timeout=int(config["llm_timeout"]))
    try:
        completion = api.chat.completions.create(
            model=os.getenv("OLLAMA_MODEL", config["llm_model"]),
            temperature=float(config["llm_temperature"]), max_tokens=output_limit,
            messages=messages,
        )
    except Exception as exc:
        # A server with smaller num_ctx than configured may still reject the request.
        error = str(exc).lower()
        if any(term in error for term in ("context length", "context window", "num_ctx", "too many tokens", "prompt too long")):
            return safe_result(
                "Сервер Ollama отклонил запрос из-за ограничения контекста. "
                "Проверьте llm_context_window и фактический num_ctx модели.",
                "context_window_exceeded", input_count, retrieval_ms,
            )
        raise

    text = completion.choices[0].message.content or ""
    used = list(dict.fromkeys(re.findall(r"\[(S\d+)\]", text)))
    invalid = [ref for ref in used if ref not in sources]
    for ref in invalid:
        text = text.replace(f"[{ref}]", "[некорректная ссылка]")
    citations = [{
        "id": ref, "source": "OpenIntro Statistics, 4th ed.",
        "section": sources[ref]["section_id"], "pdf_page": sources[ref]["pdf_page"],
        "source_file": sources[ref].get("source_file", config["source"]),
        "publication_year": sources[ref].get("publication_year"),
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
        "estimated_input_tokens": input_count, "context_window_tokens": window,
    }
