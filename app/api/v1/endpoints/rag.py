from fastapi import APIRouter

from app.schemas import RagInput
from app.globals import get_graph_retriever


router = APIRouter()


def generate_context(text, n=3):
    graph_retriever = get_graph_retriever()
    nodes = graph_retriever.retrieve(text)
    nodes_to_use = nodes[:n] if len(nodes) > n else nodes
    context_str = "\n".join(node.text for node in nodes_to_use)
    context_str = context_str.strip()

    return context_str


@router.post("/", summary="Retrieve context.")
def retrieve(rag_input: RagInput):
    rag_input = rag_input.model_dump()
    text = rag_input['text']
    context = generate_context(text)
    return {'context': context}
