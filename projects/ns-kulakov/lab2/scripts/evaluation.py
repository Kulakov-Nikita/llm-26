"""Retrieval evaluation: Recall@k, Precision@k, MRR and latency."""
import csv
import time
from config import ROOT
from io_utils import load_json
from retriever import get_retriever


def score_hits(hits, gold_section_ids, k):
    """Score at section level: duplicate chunks from a section count once."""
    ranked_sections = list(dict.fromkeys(row["section_id"] for row in hits))
    top = ranked_sections[:k]
    gold = set(gold_section_ids)
    relevant = [section for section in top if section in gold]
    first = next((rank for rank, section in enumerate(top, 1) if section in gold), None)
    return {
        f"recall@{k}": len(set(relevant)) / len(gold) if gold else 0.0,
        f"precision@{k}": len(relevant) / k,
        f"mrr@{k}": 1 / first if first else 0.0,
    }


def evaluate_retrieval(config, split="all"):
    questions = load_json("data/evaluation/questions.json")
    questions = [q for q in questions if split == "all" or q["split"] == split]
    if not questions:
        raise ValueError(f"Нет вопросов для split={split}")
    retriever = get_retriever(config)
    # Warm up the embedding model; reported latency excludes model download/loading.
    retriever.search(questions[0]["question"], 1, config["mode"])
    rows = []
    for question in questions:
        start = time.perf_counter()
        hits = retriever.search(question["question"], 10, config["mode"])
        row = {"id": question["id"], "split": question["split"],
               "latency_ms": round((time.perf_counter() - start) * 1000, 2)}
        for k in (5, 10):
            row.update(score_hits(hits, question["gold_section_ids"], k))
        rows.append(row)
    results_dir = ROOT / "results"
    results_dir.mkdir(parents=True, exist_ok=True)
    name = f"{config.get('run_id', config['preset'])}_{split}.csv"
    with (results_dir / name).open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)
    summary = []
    for subset in ("dev", "test", "all"):
        part = [row for row in rows if subset == "all" or row["split"] == subset]
        if part:
            summary.append({
                "experiment": config.get("run_id", config["preset"]), "split": subset,
                "strategy": config["strategy"], "chunk_size": config["chunk_size"],
                "overlap": config["overlap"], "mode": config["mode"],
                "embedding_model": config["embedding_model"],
                "hnsw_m": config["hnsw_m"], "hnsw_ef_construct": config["hnsw_ef_construct"],
                "hnsw_ef_search": config["hnsw_ef_search"],
                **{key: round(sum(row[key] for row in part) / len(part), 4)
                   for key in rows[0] if key.startswith(("recall@", "precision@", "mrr@", "latency_"))},
            })
    return summary


def write_comparison(rows):
    if not rows:
        raise ValueError("Нет результатов для сравнения")
    path = ROOT / "results/comparison.csv"
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)
    return path
