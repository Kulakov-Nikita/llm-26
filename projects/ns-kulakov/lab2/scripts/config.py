import hashlib
import json
from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CONFIG = ROOT / "configs" / "default.yaml"


def load_config(config_path=None, preset=None, overrides=None):
    path = Path(config_path or DEFAULT_CONFIG)
    if not path.is_absolute():
        path = ROOT / path
    config = yaml.safe_load(path.read_text(encoding="utf-8"))
    selected = preset or config["default_preset"]
    if selected not in config["experiments"]:
        raise ValueError(f"Неизвестный preset: {selected}")

    expected = dict(config)
    experiment = config["experiments"][selected]
    config.update(experiment)
    expected.update(experiment)
    for key, value in (overrides or {}).items():
        if value is not None:
            config[key] = value
    config["preset"] = selected
    config["config_path"] = str(path)

    versioned = {key: config[key] for key in (
        "source", "pages", "strategy", "chunk_size", "overlap", "include_headers",
        "mode", "embedding_model", "device", "rrf_k", "hnsw_m",
        "hnsw_ef_construct", "hnsw_ef_search")}
    unchanged = all(config.get(key) == expected.get(key) for key in versioned)
    suffix = hashlib.sha1(json.dumps(versioned, sort_keys=True).encode()).hexdigest()[:6]
    config["run_id"] = selected if unchanged else f"{selected}_{suffix}"

    if not 100 <= int(config["chunk_size"]) <= 1000:
        raise ValueError("chunk_size должен быть в диапазоне 100–1000 токенов")
    if not 0 <= int(config["overlap"]) < int(config["chunk_size"]):
        raise ValueError("overlap должен быть >= 0 и меньше chunk_size")
    if config["strategy"] not in ("recursive", "markdown"):
        raise ValueError("strategy должен быть recursive или markdown")
    if config["mode"] not in ("dense", "sparse", "hybrid"):
        raise ValueError("mode должен быть dense, sparse или hybrid")
    if int(config["hnsw_m"]) < 2 or int(config["hnsw_ef_construct"]) < 1 or int(config["hnsw_ef_search"]) < 1:
        raise ValueError("Параметры HNSW должны быть положительными, hnsw_m >= 2")
    if int(config["rrf_k"]) < 1:
        raise ValueError("rrf_k должен быть >= 1")
    if not 1 <= int(config["top_k"]) <= 20:
        raise ValueError("top_k должен быть в диапазоне 1–20")
    if int(config["max_context_tokens"]) < 1 or int(config["llm_max_tokens"]) < 1 or int(config["llm_timeout"]) < 1:
        raise ValueError("max_context_tokens, llm_max_tokens и llm_timeout должны быть положительными")
    return config
