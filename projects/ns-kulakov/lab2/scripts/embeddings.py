from functools import lru_cache


@lru_cache(maxsize=4)
def tokenizer(model_name):
    from transformers import AutoTokenizer
    result = AutoTokenizer.from_pretrained(model_name, use_fast=True)
    if not result.is_fast:
        raise ValueError("Для токенизации нужен fast tokenizer")
    return result


@lru_cache(maxsize=3)
def embedder(model_name, device):
    from sentence_transformers import SentenceTransformer
    return SentenceTransformer(model_name, device=device)
