from openai.types.chat import ChatCompletionMessageParam, ChatCompletion
from openai import OpenAI


from .._typing import OpenAPI_MODEL

__all__ = ["create_conversation"]


def create_conversation(
    client: OpenAI, messages: list[ChatCompletionMessageParam], model: OpenAPI_MODEL
) -> ChatCompletion:
    return client.chat.completions.create(messages=messages, model=model)


def calculate_message_token(
    model: OpenAPI_MODEL,
    message: ChatCompletionMessageParam,
) -> int:
    from transformers import GPT2Tokenizer

    assert "content" in message

    return len(GPT2Tokenizer.from_pretrained(model).encode(message["content"]))


def calculate_message_tokens(
    model: OpenAPI_MODEL,
    messages: list[ChatCompletionMessageParam],
):
    return sum(
        (calculate_message_token(model=model, message=message) for message in messages)
    )


def split_reply_messages(
    model: OpenAPI_MODEL,
    messages: list[ChatCompletionMessageParam],
    defualt_reply_message_token: int = 500,
):
    model_limit_token: int = get_gpt_model_token(model) - defualt_reply_message_token

    index = len(messages) - 1
    sum_token = 0

    while (model_limit_token >= sum_token) or index != 0:
        sum_token += calculate_message_token(model=model, message=messages[index])
        index -= 1

    return messages[index:]


def get_gpt_model_token(model: OpenAPI_MODEL):
    if model.startswith("gpt-3.5"):
        if "16k" in model:
            return 16_000

        return 2_048
    elif model.startswith("gpt-4"):
        if "32k" in model:
            return 32_000
        return 8_000

    raise KeyError(f"{model} is not existed")
