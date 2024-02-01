from openai import OpenAI, AsyncOpenAI
from openai.types.chat import ChatCompletionMessageParam, ChatCompletion


from ..setting import read_config_ini
from .._typing import OpenAPI_MODEL


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
    ) -> ChatCompletion:
        """
        create_conversation 傳送訊息並接收訊息

        Args:
            messages (list[ChatCompletionMessageParam]): 傳送的訊息
            model (OpenAPI_MODEL): GPT train model
            auto_save_messages (bool): 是否自動儲存messages 如果是 則會自動儲存到__MESSAGES 反之不會儲存 直接使用messages
        Returns:
            ChatCompletion: 接收的訊息
        """
        from ..openai_functools import create_conversation
        if auto_save_messages:
            self.__MESSAGES.extend(messages)
            
            return create_conversation(client=self.__client, messages=self.__MESSAGES, model=model)

        return create_conversation(client=self.__client, messages=messages, model=model)

    