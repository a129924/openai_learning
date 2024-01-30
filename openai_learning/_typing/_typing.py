from typing import Literal

from pydantic import BaseModel
from openai.types.chat import ChatCompletionMessageParam

__all__ = ["Message", "OpenAPI_MODEL"]


OpenAPI_MODEL = Literal[
    "gpt-4-0125-preview",
    "gpt-4-turbo-preview",
    "gpt-4-1106-preview",
    "gpt-4-vision-preview",
    "gpt-4",
    "gpt-4-0314",
    "gpt-4-0613",
    "gpt-4-32k",
    "gpt-4-32k-0314",
    "gpt-4-32k-0613",
    "gpt-3.5-turbo",
    "gpt-3.5-turbo-16k",
    "gpt-3.5-turbo-0301",
    "gpt-3.5-turbo-0613",
    "gpt-3.5-turbo-1106",
    "gpt-3.5-turbo-16k-0613",
]


class MessageRule(BaseModel):
    role: Literal["user"]
    content: str


class Message(BaseModel):
    """
    Message 回傳給OpenAI的message格式

    Args:
        message (list[MessageRule]): message格式
        model (OpenAPI_MODEL): 要使用什麼GPT版本
    """

    message: list[ChatCompletionMessageParam]
    model: OpenAPI_MODEL
