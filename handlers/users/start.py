from aiogram.types import Message
from aiogram.dispatcher.filters import Command, Text
from keyboards.default import menu

from loader import dp


@dp.message_handler(Command("start"))
async def bot_start(message: Message):
    await message.answer("Track the most popular crypto prices here!", reply_markup=menu)


@dp.message_handler(Text("Get prices"))
async def get_prices(message: Message):
    await message.answer("This function is in progress")
