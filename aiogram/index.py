import os
import json

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.client.default import DefaultBotProperties

bot = Bot(
    token=os.environ['BOT_TOKEN'],
    default=DefaultBotProperties(parse_mode=ParseMode.HTML),
)
dp = Dispatcher()


async def handler(event, context):
    """
    Entry point
    Точка входа в функцию
    (index.handler)
    """
    request_body_dict = json.loads(event['body'])
    await dp.feed_webhook_update(bot=bot, update=request_body_dict)
    return {
        'statusCode': 200
    }


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """
    This handler receives messages with `/start` command
    """
    await message.answer(f"Hello, <b>{message.from_user.full_name}</b>!")


@dp.message()
async def echo_handler(message: Message) -> None:
    """
    Handler will forward receive a message back to the sender
    By default, message handler will handle all message types (like a text, photo, sticker etc.)
    """
    try:
        # Send a copy of the received message
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        # But not all the types is supported to be copied so need to handle it
        await message.answer("Nice try!")
