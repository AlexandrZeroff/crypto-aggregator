from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[KeyboardButton(text='Get prices'), KeyboardButton(text='Choose tokens')]
)