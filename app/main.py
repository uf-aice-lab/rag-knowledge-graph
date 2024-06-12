import os
from fastapi import FastAPI
from llama_index.core import (
    StorageContext,
    load_index_from_storage,
    Settings,
)
from llama_index.embeddings.huggingface import HuggingFaceEmbedding

from app.api.v1.api import api_router
from app.core.config import settings
from app.globals import set_graph_index
from app.commons import OPENAI_API_KEY, PROJECT_ROOT


os.environ['OPENAI_API_KEY'] = OPENAI_API_KEY


Settings.embed_model = HuggingFaceEmbedding(
    model_name="BAAI/bge-small-en-v1.5"
)


app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

app.include_router(api_router, prefix=settings.API_V1_STR)


@app.on_event("startup")
async def load_index():
    # Load the index from storage.
    GRAPH_INDEX_PERSIST_DIR = f'{PROJECT_ROOT}/app/graph_index_storage'
    print('Loading graph index...')
    graph_index_storage_context = StorageContext.from_defaults(persist_dir=GRAPH_INDEX_PERSIST_DIR)
    graph_index = load_index_from_storage(graph_index_storage_context)
    set_graph_index(graph_index)
    print('Graph index loaded.')

