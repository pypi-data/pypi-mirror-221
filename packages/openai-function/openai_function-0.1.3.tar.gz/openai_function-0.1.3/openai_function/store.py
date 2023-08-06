import os
from dataclasses import dataclass, field
from typing import Any, AsyncGenerator, List, Type
from uuid import uuid4

import openai
from pydantic import BaseModel  # pylint: disable=no-name-in-module
from pydantic import Field  # pylint: disable=no-name-in-module

from .chat_completion import List, Literal
from .client import APIClient, APIConfig, APIException
from .logging import handle_errors, setup_logging
from .openai_functions import F, FunctionType, Optional, function_call
from .typedefs import MetaData, Vector

logger = setup_logging(__name__)


class Math(FunctionType):
    """Math operation between two numbers."""

    a: float = Field(..., description="First number.")
    b: float = Field(..., description="Second number.")
    operation: Literal[
        "add", "subtract", "multiply", "divide", "power", "root"
    ] = Field(..., description="Operation to perform.")
    result: Optional[float] = Field(
        default=None, description="Result of the operation."
    )

    async def run(self):
        """Run the function."""
        if self.operation == "add":
            self.result = self.a + self.b
        elif self.operation == "subtract":
            self.result = self.a - self.b
        elif self.operation == "multiply":
            self.result = self.a * self.b
        elif self.operation == "divide":
            self.result = self.a / self.b
        elif self.operation == "power":
            self.result = self.a**self.b
        elif self.operation == "root":
            self.result = self.a ** (1 / self.b)
        else:
            raise ValueError(f"Invalid operation: {self.operation}")
        return self.result


class UpsertVector(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid4()))
    values: Vector = Field(...)
    metadata: MetaData = Field(...)


class UpsertRequest(BaseModel):
    vectors: List[UpsertVector] = Field(..., max_items=100)
    namespace: str = Field(...)


class UpsertResponse(BaseModel):
    upsertedCount: int = Field(...)


class QueryRequest(BaseModel):
    topK: int = Field(default=4, description="The number of results to return")
    namespace: str = Field(...)
    vector: Vector = Field(...)
    includeMetadata: bool = Field(
        default=True, description="Whether to include metadata in the response"
    )


class QueryMatch(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid4()))
    score: float = Field(...)
    values: Vector = Field(...)
    metadata: MetaData = Field(...)


class QueryResponse(BaseModel):
    matches: List[QueryMatch] = Field(...)
    namespace: str = Field(...)


@dataclass
class LLMStack(APIClient):
    config: APIConfig = field(default_factory=lambda: APIConfig(base_url=os.environ.get("PINECONE_URL"), headers={"api-key": os.environ.get("PINECONE_API_KEY")}))  # type: ignore

    @handle_errors
    async def upsert_vectors(self, request: UpsertRequest) -> UpsertResponse:
        response = await self.fetch(
            "/vectors/upsert", method="POST", json=request.dict(exclude_none=True)
        )
        return UpsertResponse(**response)

    @handle_errors
    async def query_vectors(self, request: QueryRequest) -> QueryResponse:
        response = await self.fetch(
            "/query", method="POST", json=request.dict(exclude_none=True)
        )
        return QueryResponse(**response)

    @handle_errors
    async def upsert_messages(
        self,
        user_embedding: Vector,
        openai_embedding: Vector,
        prompt: str,
        text: str,
        namespace: str,
    ) -> None:
        upsert_request = UpsertRequest(
            vectors=[
                UpsertVector(values=user_embedding, metadata={"text": prompt}),
                UpsertVector(values=openai_embedding, metadata={"text": text}),
            ],
            namespace=namespace,
        )
        await self.upsert_vectors(upsert_request)

    @handle_errors
    async def chat(self, text: str) -> str:
        """Chat completion with no functions."""
        response = await openai.ChatCompletion.acreate(
            model="gpt-4-0613", messages=[{"role": "user", "content": text}]
        )
        assert isinstance(response, dict)
        return response["choices"][0]["message"]["content"]

    @handle_errors
    async def chat_with_memory(self, text: str, namespace: str = "default") -> str:
        """Chat completion with similarity search retrieval from pinecone"""
        try:
            embedding = await self.create_embeddings(text)
            query_request = QueryRequest(vector=embedding, namespace=namespace)
            query_response: QueryResponse = await self.query_vectors(query_request)
            logger.info("# of matches: %s", len(query_response.matches))  # type: ignore
            similar_text_chunks = [
                i.metadata.get("text", "") for i in query_response.matches
            ]
            similar_text = "Previous Similar results:" + "\n".join(similar_text_chunks)
            response = await openai.ChatCompletion.acreate(
                model="gpt-4-0613",
                messages=[
                    {"role": "user", "content": text},
                    {"role": "system", "content": similar_text},
                ],
            )
            assert isinstance(response, dict)
            return response["choices"][0]["message"]["content"]
        except Exception as exc:
            logger.exception(exc)
            raise APIException(message=str(exc)) from exc

    @handle_errors
    async def chat_with_functions(
        self,
        text: str,
        context: Optional[str] = None,
        functions: List[Type[F]] = FunctionType._subclasses,
    ) -> Any:
        """Chat completion with functions."""
        return await function_call(text, context=context, functions=functions)

    @handle_errors
    async def create_embeddings(self, text: str) -> Vector:
        """Creates embeddings for the given texts."""
        response = await openai.Embedding.acreate(
            engine="text-embedding-ada-002",
            input=text,
        )
        assert isinstance(response, dict)
        return response["data"][0]["embedding"]

    async def chat_stream(self, text: str) -> AsyncGenerator[str, None]:
        """Chat completion stream with no functions."""
        response = openai.ChatCompletion.acreate(
            model="gpt-4-0613",
            messages=[{"role": "user", "content": text}],
            stream=True,
        )
        assert isinstance(response, AsyncGenerator)
        async for i in response:
            assert isinstance(i, dict)
            delta = i["choices"][0]["delta"]
            if "content" in delta:
                yield delta["content"]

    async def chat_stream_with_memory(
        self, text: str, namespace: str = "default"
    ) -> AsyncGenerator[str, None]:
        """Chat completion stream with similarity search retrieval from pinecone"""
        try:
            embedding = await self.create_embeddings(text)
            query_request = QueryRequest(vector=embedding, namespace=namespace)
            query_response: QueryResponse = await self.query_vectors(query_request)
            logger.info("# of matches: %s", len(query_response.matches))  # type: ignore
            similar_text_chunks = [
                i.metadata.get("text", "") for i in query_response.matches
            ]
            similar_text = "Previous Similar results:" + "\n".join(similar_text_chunks)
            response = openai.ChatCompletion.acreate(
                model="gpt-4-0613",
                messages=[
                    {"role": "user", "content": text},
                    {"role": "system", "content": similar_text},
                ],
                stream=True,
            )
            assert isinstance(response, AsyncGenerator)
            async for i in response:
                assert isinstance(i, dict)
                delta = i["choices"][0]["delta"]
                if "content" in delta:
                    yield delta["content"]
        except Exception as exc:
            logger.exception(exc)
            raise APIException(message=str(exc)) from exc
        
    @handle_errors    
    async def chatgpt(self, text:str, namespace:str="default", context:Optional[str]=None, memory:bool=False, functions:bool=False):
        """ChatGPT4 is a function that allows you to chat with GPT-4, with the option of using memory or functions."""
        if functions:
            return await self.chat_with_functions(text, context=context)
        if memory:
            return await self.chat_with_memory(text, namespace=namespace)
        return await self.chat(text)