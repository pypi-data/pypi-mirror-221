from typing import List, Literal

from pydantic import BaseModel, Field

Role = Literal["assistant", "user","system","function"]
Model = Literal["gpt-4-0613","gpt-3-turbo-16k-0613"]

class Message(BaseModel):
    role: Role
    content:str
    
class ChatCompletionRequest(BaseModel):
    model: Model = Field(default="gpt-4-0613")
    messages: List[Message] = Field(...)
    temperature:float = Field(default=0.2, ge=0, le=1)
    max_tokens: int = Field(default=1024, ge=128, le=2048)
    
class ChatCompletionUssage(BaseModel):
    prompt_tokens:int
    completion_tokens:int
    total_tokens:int
    
class ChatCompletionChoice(BaseModel):
    index:int
    message:Message
    finish_reason:str
    
class ChatCompletionResponse(BaseModel):
    id:str
    object:str
    created:int
    model:Model
    choices:List[ChatCompletionChoice]
    usage:ChatCompletionUssage