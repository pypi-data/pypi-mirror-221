"""Open AI Functions Plugin"""
import openai
from pydantic import BaseModel, Field  # pylint: disable=no-name-in-module

from .chat_completion import (ChatCompletionChoice, ChatCompletionRequest,
                              ChatCompletionResponse, ChatCompletionUssage,
                              List, Literal, Message)
from .chat_completion import Model as ChatModel
from .chat_completion import Role
from .client import APIClient, APIConfig, APIException
from .embeddings import create_embeddings
from .logging import handle_errors, setup_logging
from .odm import FaunaClient, FaunaException, FaunaModel
from .openai_functions import FunctionType, Optional, function_call
from .vectorstore import (PineconeClient, QueryRequest, QueryResponse,
                          UpsertRequest, UpsertResponse, Vector)

logger = setup_logging(__name__)

class Math(FunctionType):
    """Math operation between two numbers."""
    a: float = Field(..., description="First number.")
    b: float = Field(..., description="Second number.")
    operation: Literal["add", "subtract", "multiply", "divide", "power","root"] = Field(..., description="Operation to perform.")
    result: Optional[float] = Field(default=None, description="Result of the operation.")
    
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
            self.result = self.a ** self.b
        elif self.operation == "root":
            self.result = self.a ** (1/self.b)
        else:
            raise ValueError(f"Invalid operation: {self.operation}")
        return self.result
   
    
async def chat(text: str) -> str:
    """Chat completion with no functions."""
    response = await openai.ChatCompletion.acreate(
        model="gpt-4-0613", messages=[{"role": "user", "content": text}]
    )
    assert isinstance(response, dict)
    return response["choices"][0]["message"]["content"]


@handle_errors
async def chat_with_memory(text: str, pinecone:PineconeClient, namespace: str = "default") -> str:
    """Chat completion with similarity search retrieval from pinecone"""
    try:
        embedding = await create_embeddings(text)
        query_request = QueryRequest(vector=embedding, namespace=namespace)
        query_response: QueryResponse = await pinecone.query_vectors(query_request)
        pinecone.logger.info("# of matches: %s", len(query_response.matches))  # type: ignore
        similar_text_chunks = [i.metadata.get("text", "") for i in query_response.matches]
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
async def chat_with_functions(text: str):
    """Chat completion with functions."""
    return await function_call(text)
