from openai_learning.app import OpenAIClient


if __name__ == "__main__":
    client = OpenAIClient()

    stream = client.create_conversation(
        messages=[
            {
                "role": "user",
                "content": "Say this is a test",
            },
        ],
        model="gpt-3.5-turbo",
    )

    client.print_stream(stream)
