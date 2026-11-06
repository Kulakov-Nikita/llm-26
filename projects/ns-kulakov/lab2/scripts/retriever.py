import re
from functools import lru_cache
import numpy as np
from io_utils import read_jsonl
from build_index import index_path
from embeddings import embedder
from load_to_vector_store import client, collection_name

EN = {
    "первого рода": "type i error", "второго рода": "type ii error",
    "нулев": "null", "альтернатив": "alternative", "практическ": "practical",
    "статистическ": "statistical", "значим": "significance significant",
    "мощност": "power", "размер выборки": "sample size", "выборк": "sample sampling",
    "одновыборочн": "one sample", "парн": "paired", "независим": "independent",
    "средн": "mean", "допущен": "assumption", "предпосыл": "assumption condition",
    "групп": "group", "анова": "anova", "категориальн": "categorical",
    "перемен": "variable", "соглас": "goodness fit", "частот": "frequency",
    "наблюдаем": "observed", "ожидаем": "expected", "распределен": "distribution",
    "доверительн": "confidence interval", "уровень доверия": "confidence level",
    "корреляц": "correlation", "дисперс": "variance", "сравнен": "compare difference",
    "тест": "test", "критери": "test", "дол": "proportion", "ошиб": "error",
    "эффект": "effect", "аппроксимац": "approximation", "нормальн": "normal",
    "маленьк": "small", "мал": "small", "успешн": "success", "исход": "outcome",
    "вывод": "inference", "точечн": "point estimate", "вероятност": "probability",
}


def words(text):
    tokens = re.findall(r"[a-z]+|\d+", text.casefold())
    if "χ" in text.casefold() or "хи-квадрат" in text.casefold():
        tokens.extend(("chi", "square"))
    return tokens


class Retriever:
    def __init__(self, config):
        self.config = config
        self.chunks = read_jsonl(index_path(config) / "chunks.jsonl")
        self.bm25 = None

    def search(self, query, k=5, mode=None):
        from qdrant_client import models
        mode = mode or self.config["mode"]
        if mode not in ("dense", "sparse", "hybrid"):
            raise ValueError("mode must be dense, sparse, or hybrid")
        count = max(30, 5 * k) if mode == "hybrid" else k
        dense = []
        if mode != "sparse":
            vector = embedder(self.config["embedding_model"], self.config["device"]).encode(
                [query], normalize_embeddings=True)[0]
            points = client(self.config).query_points(
                collection_name=collection_name(self.config), query=vector.tolist(), limit=count,
                with_payload=True,
                search_params=models.SearchParams(hnsw_ef=int(self.config["hnsw_ef_search"])),
            ).points
            dense = [{**point.payload, "score": float(point.score)} for point in points]
        if mode == "dense":
            return dense[:k]
        if self.bm25 is None:
            from rank_bm25 import BM25Okapi
            self.bm25 = BM25Okapi([words(row["text"]) for row in self.chunks])
        expanded = words(query) + [word for root, value in EN.items() if root in query.lower() for word in value.split()]
        scores = self.bm25.get_scores(expanded) if expanded else np.zeros(len(self.chunks))
        order = np.argsort(-scores, kind="stable")[:count]
        sparse = [{**self.chunks[i], "score": float(scores[i])} for i in order if scores[i] > 0]
        if mode == "sparse":
            return sparse[:k]
        fused = {}
        for group in (dense, sparse):
            for rank, row in enumerate(group, 1):
                cid = row["chunk_id"]
                if cid not in fused:
                    fused[cid] = {**row, "score": 0.0}
                fused[cid]["score"] += 1 / (int(self.config["rrf_k"]) + rank)
        return sorted(fused.values(), key=lambda row: -row["score"])[:k]


@lru_cache(maxsize=8)
def _cached_retriever(config_json):
    import json
    return Retriever(json.loads(config_json))


def get_retriever(config):
    import json
    return _cached_retriever(json.dumps(config, sort_keys=True, default=str))
