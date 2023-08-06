"""Embeddings module."""
from typing import List, Literal

import openai

Model = Literal["text-embedding-ada-002"]
Vector = List[float]


async def create_embeddings(
    text: str, model: Model = "text-embedding-ada-002"
) -> Vector:
    """Creates embeddings for the given texts."""
    response = await openai.Embedding.acreate(
        engine=model,
        input=text,
    )
    assert isinstance(response, dict)
    return response["data"][0]["embedding"]
