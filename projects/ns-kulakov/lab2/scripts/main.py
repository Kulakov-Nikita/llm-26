import sys
import argparse
import json

from config import load_config
from build_index import build_index, parse_documents
from load_to_vector_store import load_to_vector_store
from evaluation import evaluate_retrieval, write_comparison
from pipeline import answer


if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise SystemExit("Команды: parse, build, load, evaluate, compare, search, ask, serve")
    command = sys.argv.pop(1)
    if command not in {"parse", "build", "load", "evaluate", "compare", "search", "ask", "serve"}:
        raise SystemExit(f"Неизвестная команда: {command}")

    parser = argparse.ArgumentParser(description=f"Lab 2: {command}")
    parser.add_argument("--config", default=None)
    parser.add_argument("--preset", default=None)
    parser.add_argument("--strategy", choices=["recursive", "markdown"])
    parser.add_argument("--chunk-size", type=int)
    parser.add_argument("--overlap", type=int)
    parser.add_argument("--headers", choices=["yes", "no"])
    parser.add_argument("--embedding-model")
    parser.add_argument("--device", choices=["cpu", "cuda"])
    parser.add_argument("--mode", choices=["dense", "sparse", "hybrid"])
    parser.add_argument("--qdrant-url")
    parser.add_argument("--hnsw-m", type=int)
    parser.add_argument("--hnsw-ef-construct", type=int)
    parser.add_argument("--hnsw-ef-search", type=int)
    parser.add_argument("--top-k", type=int)
    parser.add_argument("--split", choices=["all", "dev", "test"], default="all")
    parser.add_argument("--rebuild", action="store_true")
    parser.add_argument("--reset", action="store_true")
    if command in ("ask", "search"):
        parser.add_argument("question")
    args = parser.parse_args()
    overrides = {
        "strategy": args.strategy, "chunk_size": args.chunk_size, "overlap": args.overlap,
        "include_headers": None if args.headers is None else args.headers == "yes",
        "embedding_model": args.embedding_model, "device": args.device, "mode": args.mode,
        "qdrant_url": args.qdrant_url, "hnsw_m": args.hnsw_m,
        "hnsw_ef_construct": args.hnsw_ef_construct, "hnsw_ef_search": args.hnsw_ef_search,
        "top_k": args.top_k,
    }
    overrides = {key: value for key, value in overrides.items() if value is not None}
    if command == "compare":
        experiment_keys = {"strategy", "chunk_size", "overlap", "include_headers", "mode", "top_k"}
        conflicts = sorted(experiment_keys.intersection(overrides))
        if conflicts:
            parser.error("Для compare нельзя переопределять параметры экспериментов: " + ", ".join(conflicts))
        overrides = {key: value for key, value in overrides.items()
                     if key in {"embedding_model", "device", "qdrant_url", "hnsw_m", "hnsw_ef_construct", "hnsw_ef_search"}}
    config = load_config(args.config, args.preset, overrides)

    match command:
        case "parse":
            print(f"Извлечено страниц: {parse_documents(config)}")
        case "build":
            print(f"Индекс: {build_index(config, rebuild=args.rebuild)}")
        case "load":
            print(f"Qdrant: {load_to_vector_store(config, reset=args.reset or args.rebuild, rebuild=args.rebuild)}")
        case "evaluate":
            print(json.dumps(evaluate_retrieval(config, args.split), ensure_ascii=False, indent=2))
        case "compare":
            rows = []
            for preset in config["compare_presets"]:
                experiment = load_config(args.config, preset, overrides)
                load_to_vector_store(experiment, reset=args.reset or args.rebuild, rebuild=args.rebuild)
                rows.extend(evaluate_retrieval(experiment))
            print(f"Сравнение сохранено: {write_comparison(rows)}")
        case "ask" | "search":
            result = answer(args.question, config, args.top_k, args.mode, generate=(command == "ask"))
            print(json.dumps(result, ensure_ascii=False, indent=2))
        case "serve":
            import uvicorn
            from app import app
            app.state.config = config
            uvicorn.run(app, host=config["api_host"], port=int(config["api_port"]))