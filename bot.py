"""
Copyright 2022 kensoi
"""
import asyncio
from os import environ
from dotenv import load_dotenv
from vkbotkit import ToolKit


PEER_ID = 1

async def main():
    """
    Главная функция приложения
    """

    tools = ToolKit(environ['DEBUG_TOKEN'], environ['GROUP_ID'])
    tools.configure_logger()

    att = await tools.uploader.document("graffiti.png", None, None, PEER_ID, "graffiti")
    print(att)
    await send_message(tools, None, att)
    await send_message(tools, "вечер в хату собаки")


async def send_message(tools:ToolKit = None, message: str = None, attachment: str = None):
    """
    Отправить сообщение
    """
    await tools.api.messages.send(
        random_id = tools.gen_random(),
        peer_id = PEER_ID,
        message = message,
        attachment = attachment)


if __name__ == "__main__":
    load_dotenv()
    loop = asyncio.new_event_loop()
    loop.run_until_complete(main())
