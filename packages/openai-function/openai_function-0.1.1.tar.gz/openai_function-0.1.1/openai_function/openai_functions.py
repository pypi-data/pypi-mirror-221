"""OpenAI Function constructs"""
import json
from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional, Type, TypeVar

import openai
from pydantic import BaseModel, Field  # pylint: disable=no-name-in-module

from .chat_completion import Message, Model
from .logging import log


class FunctionRequest(BaseModel):
    """
    Defines a function request.
    """

    model: Model = Field(
        default="gpt-4-0613", description="The model used for the chat completion."
    )
    messages: List[Message] = Field(
        ..., description="The list of messages in the conversation."
    )
    functions: Optional[List[Dict[str, Any]]] = Field(
        None, description="Optional list of functions to be used."
    )


@log
class FunctionType(BaseModel, ABC):
    _subclasses: List[Type["FunctionType"]] = []

    @classmethod
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        _schema = cls.schema()
        if cls.__doc__ is None:
            raise ValueError(
                f"FunctionType subclass {cls.__name__} must have a docstring"
            )
        cls.openaischema = {
            "name": cls.__name__,
            "description": cls.__doc__,
            "parameters": {
                "type": "object",
                "properties": _schema["properties"],
                "required": _schema["required"],
            },
        }
        cls.logger.info(f"\tRegistered function {cls.__name__}")  # type: ignore # pylint: disable=no-member
        cls._subclasses.append(cls)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.logger.info(f"Function {self.__class__.__name__} called with {kwargs}")  # type: ignore # pylint: disable=no-member
        self.logger.info(f"Function {self.__class__.__name__} initialized")  # type: ignore # pylint: disable=no-member

    @abstractmethod
    async def run(self) -> Any:
        ...


F = TypeVar("F", bound=FunctionType)


async def parse_openai_response(  # pylint: disable=dangerous-default-value
    response: dict,
    functions: List[
        Type[F]
    ] = FunctionType._subclasses,  # pylint: disable=protected-access
) -> Any:
    """Parse the response from OpenAI and return the result."""
    choice = response["choices"][0]["message"]
    if "function_call" in choice:
        function_call_ = choice["function_call"]
        name = function_call_["name"]
        arguments = function_call_["arguments"]
        for i in functions:
            if i.__name__ == name:
                result = await i.run(i(**json.loads(arguments)))
                break
        else:
            raise ValueError(f"Function {name} not found")
        return result
    return choice["content"]


async def function_call(  # pylint: disable=dangerous-default-value
    text: str,
    context: Optional[str] = None,
    model: Model = "gpt-4-0613",
    functions: List[
        Type[F]
    ] = FunctionType._subclasses,  # pylint: disable=protected-access
) -> Any:
    """
    Function to call a OpenAI function with given text and context.

    Arguments:
    text -- Input text for the function
    context -- Optional context for the function
    model -- Model to be used. Defaults to "gpt-4-0613"
    functions -- List of function types. Defaults to all subclasses of FunctionType.
    """
    if context is None:
        messages = [Message(role="user", content=text)]
    else:
        messages = [
            Message(role="system", content=context),
            Message(role="user", content=text),
        ]
    data = FunctionRequest(
        model=model, messages=messages, functions=[i.openaischema for i in functions]
    ).dict()
    response = await openai.ChatCompletion.acreate(**data)
    assert isinstance(response, dict)
    return await parse_openai_response(response, functions=functions)
