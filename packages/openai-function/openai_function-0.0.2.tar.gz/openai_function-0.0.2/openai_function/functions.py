import json
from abc import ABC, abstractmethod
from typing import *

import openai
from pydantic import BaseModel, Field

from .chat_completion import Message


class FunctionRequest(BaseModel):
    model: str = Field(default="gpt-4-0613")
    messages: List[Message] = Field(...)


class FunctionType(BaseModel):
    @classmethod
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        _schema = cls.schema()
        if cls.__doc__ is None:
            raise ValueError(f"FunctionType subclass {cls.__name__} must have a docstring")
        cls.openaischema = {
            "name": cls.__name__,
            "description":cls.__doc__,
            "parameters": {
                "type": "object",
                "properties": _schema["properties"],
                "required": _schema["required"]
            },
        }
        
    @abstractmethod
    async def run(self)->Any:
        ...

F = TypeVar("F", bound=FunctionType)
 
async def function_call(text:str,functions:List[Type[F]]):
    data = {
        "model": "gpt-4-0613",
        "messages":[{
                "role": "user",
                "content": text
            }],
        "functions": [i.openaischema for i in functions]
    }
    
    response = await openai.ChatCompletion.acreate(**data)
    assert isinstance(response,dict)
    if "function_call" in response['choices'][0]['message']:
        call_struct = response['choices'][0]['message']['function_call']
        name = call_struct['name']
        arguments = call_struct['arguments']
        for i in functions:
            if i.__name__ == name:
                result = await i.run(i(**json.loads(arguments)))
                break
        else:
            raise ValueError(f"Function {name} not found")
        return result
    else:
        return response['choices'][0]['message']['content']