from openai import OpenAI, AsyncOpenAI
from openai.types.chat import ChatCompletionMessageParam, ChatCompletion


from ..setting import read_config_ini
from .._typing import OpenAPI_MODEL

__all__ = ["OpenAIClient"]


class OpenAIClient:
    def __init__(
        self, openai_key: str = read_config_ini()["OPENAPI_SETTING"]["API_KEY"]
    ):
        self.__client = OpenAI(api_key=openai_key)

    def create_message(
        self,
        messages: list[ChatCompletionMessageParam],
        model: OpenAPI_MODEL,
    ) -> ChatCompletion:
        """
        create_message 傳送訊息並接收訊息

        Args:
            messages (list[ChatCompletionMessageParam]): 傳送的訊息
            model (OpenAPI_MODEL): GPT train model

        Returns:
            ChatCompletion: 接收的訊息
        """
        return self.__client.chat.completions.create(messages=messages, model=model)
