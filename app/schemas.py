from pydantic import BaseModel


class RagInput(BaseModel):
    text: str

