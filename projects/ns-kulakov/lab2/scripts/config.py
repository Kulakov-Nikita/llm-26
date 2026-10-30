import hashlib
import json
import os
from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CONFIG = ROOT / "configs" / "default.yaml"


def load_config(config_path=None, preset=None):
    path = Path(config_path or DEFAULT_CONFIG)
    if not path.is_absolute():
        path = ROOT / path
    config = yaml.safe_load(path.read_text(encoding="utf-8"))
    selected = preset or config["default_preset"]
    if selected not in config["experiments"]:
        raise ValueError(f"Неизвестный preset: {selected}")
    config.update(config["experiments"][selected])
    config["preset"] = selected
    config["config_path"] = str(path)

    versioned = {key: config[key] for key in (
        "strategy", "chunk_size", "overlap", "include_headers", "mode", "embedding_model",
        "hnsw_m", "hnsw_ef_construct", "hnsw_ef_search")}
    default_experiment = config["experiments"][selected]
    unchanged = all(config.get(key) == value for key, value in default_experiment.items())
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
    return config
