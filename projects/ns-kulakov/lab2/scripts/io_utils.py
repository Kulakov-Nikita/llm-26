import hashlib
import json
from pathlib import Path
from config import ROOT


def project_path(path):
    path = Path(path)
    return path if path.is_absolute() else ROOT / path


def load_json(path):
    return json.loads(project_path(path).read_text(encoding="utf-8"))


def save_json(path, value):
    path = project_path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2), encoding="utf-8")


def read_jsonl(path):
    return [json.loads(line) for line in project_path(path).read_text(encoding="utf-8").splitlines() if line.strip()]


def write_jsonl(path, rows):
    path = project_path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("".join(json.dumps(row, ensure_ascii=False) + "\n" for row in rows), encoding="utf-8")


def file_sha256(path):
    return hashlib.sha256(project_path(path).read_bytes()).hexdigest()
