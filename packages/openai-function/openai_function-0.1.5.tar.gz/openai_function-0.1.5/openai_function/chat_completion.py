"""Chat Completions Schemas"""
from typing import List, Literal

from pydantic import BaseModel, Field  # pylint: disable=no-name-in-module

Role = Literal["assistant", "user", "system", "function"]
Model = Literal["gpt-4-0613", "gpt-3.5-turbo-16k-0613"]


class Message(BaseModel):
    """Defines a message within a conversation."""

    role: Role = Field(..., description="The role of the message.")
    content: str = Field(..., description="The content of the message.")


class ChatCompletionRequest(BaseModel):
    """Defines a request for a chat completion."""

    model: Model = Field(
        default="gpt-4-0613", description="The model used for the chat completion."
    )
    messages: List[Message] = Field(
        ..., description="The list of messages in the conversation."
    )
    temperature: float = Field(
        default=0.2,
        ge=0,
        le=1,
        description="The temperature for the chat completion. Higher values make output more random.",  # pylint: disable=line-too-long
    )
    max_tokens: int = Field(
        default=1024,
        ge=128,
        le=2048,
        description="The maximum number of tokens in the output.",
    )
    stream: bool = Field(default=False, description="Whether the response is a stream.")


class ChatCompletionUssage(BaseModel):
    """Defines the usage of the tokens for a chat completion."""

    prompt_tokens: int = Field(
        ..., description="The number of tokens used in the prompt."
    )
    completion_tokens: int = Field(
        ..., description="The number of tokens used in the completion."
    )
    total_tokens: int = Field(..., description="The total number of tokens used.")


class ChatCompletionChoice(BaseModel):
    """Defines a choice in a chat completion."""

    index: int = Field(..., description="The index of the choice.")
    message: Message = Field(..., description="The message of the choice.")
    finish_reason: str = Field(..., description="The reason for the finish.")


class ChatCompletionResponse(BaseModel):
    """Defines a response for a chat completion."""

    id: str = Field(..., description="The id of the response.")
    object: str = Field(..., description="The object of the response.")
    created: int = Field(..., description="The time when the response was created.")
    model: Model = Field(..., description="The model used for the chat completion.")
    choices: List[ChatCompletionChoice] = Field(
        ..., description="The list of choices in the response."
    )
    usage: ChatCompletionUssage = Field(
        ..., description="The usage of the tokens in the response."
    )
    stream: bool = Field(default=False, description="Whether the response is a stream.")
