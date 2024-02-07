from openai import OpenAI, AsyncOpenAI

from ..setting import read_config_ini
from .._typing import OpenAPI_MODEL, ChatResponse, ChatCompletionMessageParam, Stream


__all__ = ["OpenAIClient"]


class OpenAIClient:
    __MESSAGES: list[ChatCompletionMessageParam] = []

    def __init__(
        self, openai_key: str = read_config_ini()["OPENAPI_SETTING"]["API_KEY"]
    ):
        self.__client = OpenAI(api_key=openai_key)

    def create_conversation(
        self,
        messages: list[ChatCompletionMessageParam],
        model: OpenAPI_MODEL,
        auto_save_messages: bool = True,
    ) -> ChatResponse:
        """
        create_conversation 傳送訊息並接收訊息

        Args:
            messages (list[ChatCompletionMessageParam]): 傳送的訊息
            model (OpenAPI_MODEL): GPT train model
            auto_save_messages (bool): 是否自動儲存messages 如果是 則會自動儲存到__MESSAGES 反之不會儲存 直接使用messages
        Returns:
            ChatCompletion: 接收的訊息

        ## Example :
        ```python=
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": "Say this is a test",
                }
            ],
            model="gpt-3.5-turbo",
        )
        ```
        """
        from ..openai_functools import create_conversation

        working_messages = self.__MESSAGES if auto_save_messages else messages

        if auto_save_messages:
            self.__MESSAGES.extend(messages)

        # working_messages = split_reply_messages(model=model, messages=working_messages)

        return create_conversation(
            client=self.__client, messages=working_messages, model=model
        )

    def print_stream(self, stream: ChatResponse) -> None:
        if isinstance(stream, Stream):
            for chunk in stream:
                print(chunk.choices[0].delta.content)

        else:
            print(stream.choices[0].message)
