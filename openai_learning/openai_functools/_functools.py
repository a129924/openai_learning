from openai.types.chat import ChatCompletionMessageParam, ChatCompletion
from openai import OpenAI

from .._typing import OpenAPI_MODEL

__all__ = ["create_conversation"]


def create_conversation(
    client: OpenAI, messages: list[ChatCompletionMessageParam], model: OpenAPI_MODEL
) -> ChatCompletion:
    return client.chat.completions.create(messages=messages, model=model)
