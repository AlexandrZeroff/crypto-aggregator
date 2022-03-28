from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from .callbacks import price_callback, change_coin_list_callback

coins = InlineKeyboardMarkup(row_width=2)
coin_buttons = [
    InlineKeyboardButton(text="BTC", callback_data='price:btc'),
    InlineKeyboardButton(text="ETH", callback_data='price:eth'),
    InlineKeyboardButton(text="BNB", callback_data='price:bnb'),
    InlineKeyboardButton(text="SOL", callback_data='price:sol'),
    InlineKeyboardButton(text="1INCH", callback_data='price:1inch'),
    InlineKeyboardButton(text="NEAR", callback_data='price:near'),
    InlineKeyboardButton(text="FIL", callback_data='price:fil'),
    InlineKeyboardButton(text="TWT", callback_data='price:twt'),
    InlineKeyboardButton(text="Select coins", callback_data='change_coin_list')
]
coins.add(*coin_buttons)