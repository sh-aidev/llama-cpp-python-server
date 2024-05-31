# Adapted from
# https://github.com/lm-sys/FastChat/blob/168ccc29d3f7edc50823016105c024fe2282732a/fastchat/protocol/openai_api_protocol.py
import time
import uuid
from typing import Any, Dict, List, Literal, Optional, Union, Annotated
from fastapi import File

from pydantic import BaseModel, Field


def random_uuid() -> str:
    return str(uuid.uuid4().hex)


class UsageInfo(BaseModel):
    prompt_tokens: int = 0
    total_tokens: int = 0
    completion_tokens: Optional[int] = 0


class ChatCompletionRequest(BaseModel):
    id: str = Field(default_factory=lambda: f"chatcmpl-{random_uuid()}")
    model: str = "gpt-3.5-turbo"
    messages: List[Dict[str,Any]]
    temperature: Optional[float] = 0.7
    top_p: Optional[float] = 1.0
    n: Optional[int] = 1
    max_tokens: Optional[int] = 256
    user: Optional[str] = None
    best_of: Optional[int] = None
    top_k: Optional[int] = -1
    use_beam_search: Optional[bool] = False
    grammar: Optional[str] = None


class ChatCompletionMessage(BaseModel):
    content: str
    role: str
    function_call: Optional[str] = None
    tool_calls: Optional[List[str]] = None


class Choice(BaseModel):
    finish_reason: str
    index: int
    logprobs: Optional[Dict[str, List[float]]] = None
    message: ChatCompletionMessage

class ChatCompletionResponse(BaseModel):
    id: str = Field(default_factory=lambda: f"chatcmpl-{random_uuid()}")
    object: str = "chat.completion"
    created: int = Field(default_factory=lambda: int(time.time()))
    model: str
    choices: List[Choice]
    system_fingerprint: Optional[str] = None
    usage: UsageInfo

class EmbeddingRequest(BaseModel):
    id: str = Field(default_factory=lambda: f"embedding-{random_uuid()}")
    text: Union[str, List[str]]
    model: str = "text-embedding-ada-002"

class Embedding(BaseModel):
    embedding: List[float]
    index: int
    object: str = "embedding"

class CreateEmbeddingResponse(BaseModel):
    data: List[Embedding]
    model: str
    object: str = "list"
    usage: UsageInfo