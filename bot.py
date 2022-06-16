"""
Bot application
"""
import asyncio
from os import environ
from dotenv import load_dotenv
from vkbotkit import ToolKit


async def main():
    """
    главная функция приложения
    """
    
    tools = ToolKit(environ['DEBUG_TOKEN'])
    tools.configure_logger()

    response = await tools.uploader.document("graffiti.png", None, None, 517114114, "graffiti")
    att = f"doc{response.graffiti.owner_id}_{response.graffiti.id}"

    await send_message(tools, None, att)
    await send_message(tools, "вечер в хату собаки")


async def send_message(tools:ToolKit = None, message: str = None, attachment: str = None):
    """
    Отправить сообщение
    """
    await tools.api.messages.send(
        random_id = tools.gen_random(), 
        peer_id = 2000000007, 
        message = message,
        attachment = attachment)

        
if __name__ == "__main__":
    load_dotenv()
    loop = asyncio.new_event_loop()
    loop.run_until_complete(main())
