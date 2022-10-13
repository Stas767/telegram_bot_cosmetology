from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton
)

b1 = KeyboardButton('Услуги')
b2 = KeyboardButton('Запись')
b3 = KeyboardButton('Режим работы')
b4 = KeyboardButton('Контакты')
b5 = KeyboardButton('Мои записи')

kb_client = ReplyKeyboardMarkup(
    resize_keyboard=True,
    # one_time_keyboard=True
)

kb_client.add(b1).insert(b2).row(b3, b4, b5)
# kb_client.row_width(b1, b2, b3, b4, b5)
