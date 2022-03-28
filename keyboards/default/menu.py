from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def set_menu_keyboard():
    menu = ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ['Get current price', 'Get price history']
    menu.add(*buttons)
    return menu

menu = set_menu_keyboard()