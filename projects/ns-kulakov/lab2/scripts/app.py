from fastapi import FastAPI
from pydantic import BaseModel, Field
from config import ROOT, load_config
from build_index import index_path
from pipeline import answer
from load_to_vector_store import collection_name

app = FastAPI(title="ReproLab RAG API", version="1.0")
app.state.config = None


class Question(BaseModel):
    question: str = Field(min_length=1)
    top_k: int | None = Field(default=None, ge=1, le=20)


def current_config():
    return app.state.config or load_config()


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/index/info")
def index_info():
    config = current_config()
    return {"preset": config["preset"], "index_path": str(index_path(config).relative_to(ROOT)),
            "collection": collection_name(config)}


@app.post("/search")
def search_api(body: Question):
    return answer(body.question, current_config(), body.top_k, generate=False)


@app.post("/ask")
def ask_api(body: Question):
    return answer(body.question, current_config(), body.top_k)
