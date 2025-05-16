from aiogram.types import KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder
def get_find():
    builder = ReplyKeyboardBuilder()
    builder.add(KeyboardButton(text="Отследить сайт"))
    builder.adjust(1)
    return builder.as_markup(resize_keyboard=True)

def get_skrin():
    builder = ReplyKeyboardBuilder()
    builder.add(KeyboardButton(text="Да"))
    builder.add(KeyboardButton(text="Нет"))
    builder.adjust(1)
    return builder.as_markup(resize_keyboard=True)  