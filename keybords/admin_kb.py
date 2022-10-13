from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton
)


button_load = KeyboardButton('Добавить новую услугу')
button_delete = ('/Удалить')

button_case_admin = ReplyKeyboardMarkup(
    resize_keyboard=True
).row(button_load, button_delete)
