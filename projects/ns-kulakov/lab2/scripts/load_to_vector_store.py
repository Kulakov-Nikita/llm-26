from functools import lru_cache
from uuid import NAMESPACE_URL, uuid5
import numpy as np
from qdrant_client import QdrantClient

from io_utils import read_jsonl
from build_index import build_index, index_path


@lru_cache(maxsize=2)
def _client(url):
    from qdrant_client import QdrantClient
    return QdrantClient(url=url, timeout=60)


def client(config):
    return _client(config["qdrant_url"])


def collection_name(config):
    return f"reprolab_{index_path(config).name}_m{config['hnsw_m']}_ef{config['hnsw_ef_construct']}"


def load_to_vector_store(config, reset=False):
    from qdrant_client import models
    directory = build_index(config)
    chunks = read_jsonl(directory / "chunks.jsonl")
    vectors = np.load(directory / "vectors.npy", mmap_mode="r")
    db = QdrantClient(url=config["qdrant_url"], timeout=60)
    name = collection_name(config)
    if reset and db.collection_exists(name):
        db.delete_collection(name)
    if not db.collection_exists(name):
        db.create_collection(
            collection_name=name,
            vectors_config=models.VectorParams(size=vectors.shape[1], distance=models.Distance.COSINE),
            hnsw_config=models.HnswConfigDiff(m=int(config["hnsw_m"]), ef_construct=int(config["hnsw_ef_construct"])),
        )
    for start in range(0, len(chunks), 64):
        points = [models.PointStruct(
            id=str(uuid5(NAMESPACE_URL, row["chunk_id"])), payload=row, vector=vectors[i].tolist())
            for i, row in enumerate(chunks[start:start + 64], start)]
        db.upsert(collection_name=name, wait=True, points=points)
    count = db.count(name, exact=True).count
    if count != len(chunks):
        raise RuntimeError(f"В Qdrant {count} точек, ожидалось {len(chunks)}; используй --reset")
    return name, len(chunks)
