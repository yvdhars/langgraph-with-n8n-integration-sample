import chainlit as cl
import requests

API_URL = "http://127.0.0.1:8001/chat"

@cl.on_message
async def main(message: cl.Message):

    response = requests.post(
        API_URL,
        json={
            "message": message.content
        }
    )

    answer = response.json()["response"]

    await cl.Message(
        content=answer
    ).send()