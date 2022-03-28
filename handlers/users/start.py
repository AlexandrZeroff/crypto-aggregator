from aiogram.types import Message
from aiogram.utils.callback_data import CallbackData
from aiogram.types import CallbackQuery
from aiogram.dispatcher.filters import Command, Text
from matplotlib import text
from keyboards.default import menu
from apis.prices import CryptoCompare

from loader import dp
from keyboards.inline.coins import coins
from keyboards.inline.callbacks import price_callback

cryptocompare = CryptoCompare()

@dp.message_handler(Command("start"))
async def bot_start(message: Message):
    await message.answer("Track the most popular crypto prices here!", reply_markup=menu)


@dp.message_handler(Text("Get current price"))
async def get_prices(message: Message):
    await message.answer("Data is provided by CryptoCompare (inc. CCCAGG). \n\n💰Select coin from list below:", reply_markup=coins)


@dp.callback_query_handler(text_contains='price:')
async def get_coin_price(call:CallbackQuery):
    await call.answer(cache_time=60)
    coin = call.data.split(':')[1]
    
    api_response = cryptocompare.get_price(coin).get('USDT')
    
    await call.message.edit_text(f'Data is provided by CryptoCompare (inc. CCCAGG).\n\nCurrent {coin.upper()} price is {api_response}$\n\n💰Select coin from list below:', reply_markup=coins)


