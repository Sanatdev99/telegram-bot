from aiogram.types import ReplyKeyboardMarkup, KeyboardButton,InlineKeyboardMarkup, InlineKeyboardButton
from configs import CATEGORIES

def buttons_category():
    buttons = [[KeyboardButton(text=category)] for category in CATEGORIES.keys()]
    markup = ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)
    return markup

def button_link(link):
    markup =InlineKeyboardMarkup()
    btn = InlineKeyboardButton(text='Batafsil',url=link)
    markup.add(btn)
    return markup
