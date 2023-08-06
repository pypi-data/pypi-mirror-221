import os
from dataclasses import dataclass, field
from typing import List
from uuid import uuid4

from pydantic import BaseModel, Field  # pylint: disable=no-name-in-module

from .client import APIClient, APIConfig
from .logging import handle_errors, setup_logging
from .typedefs import MetaData, Vector


class UpsertVector(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid4()))
    values:Vector = Field(...)
    metadata: MetaData = Field(...)
    
class UpsertRequest(BaseModel):
    vectors: List[UpsertVector] = Field(..., max_items=100)
    namespace:str = Field(...)
    
class UpsertResponse(BaseModel):
    upsertedCount: int = Field(...)
    
class QueryRequest(BaseModel):
    topK: int = Field(default=4, description="The number of results to return")
    namespace: str = Field(...)
    vector: Vector = Field(...)
    includeMetadata: bool = Field(default=True, description="Whether to include metadata in the response")
    
class QueryMatch(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid4()))
    score: float = Field(...)
    values: Vector = Field(...)
    metadata: MetaData = Field(...)
    
class QueryResponse(BaseModel):
    matches: List[QueryMatch] = Field(...)
    namespace: str = Field(...)
    
@dataclass
class PineconeClient(APIClient):
    config:APIConfig = field(default_factory=lambda: APIConfig(base_url=os.environ.get("PINECONE_URL"), headers={"api-key": os.environ.get("PINECONE_API_KEY")})) # type: ignore
    @handle_errors
    async def upsert_vectors(self,request: UpsertRequest) -> UpsertResponse:
        response = await self.fetch("/vectors/upsert", method="POST", json=request.dict(exclude_none=True))
        return UpsertResponse(**response)
    @handle_errors
    async def query_vectors(self,request: QueryRequest) -> QueryResponse:
        response = await self.fetch("/query", method="POST", json=request.dict(exclude_none=True))
        return QueryResponse(**response)
    
    @handle_errors
    async def upsert_vectors_to_pinecone(self, user_embedding:Vector, openai_embedding:Vector, prompt:str, text:str, namespace:str)->None:
        upsert_request = UpsertRequest(
            vectors=[
                UpsertVector(values=user_embedding, metadata={"text": prompt}),
                UpsertVector(values=openai_embedding, metadata={"text": text})
            ],
            namespace=namespace
        )
        await self.upsert_vectors(upsert_request)
