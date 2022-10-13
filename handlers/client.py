from aiogram import Dispatcher, types

from core import bot, dp
from keybords.client_kb import kb_client


# @dp.message_handler(commands=['start', 'help'])
async def commands_start(message: types.Message):
    await bot.send_message(
        message.from_user.id,
        'Добро пожаловать! Чем я могу помочь?',
        reply_markup=kb_client
    )


# @dp.message_handler(commands=['Услуги'])
async def list_services(message: types.Message):
    await bot.send_message(
        message.from_user.id,
        'Список процедур, нужно будет сделать карточки для всех'
    )


# @dp.message_handler(commands=['Запись'])
async def recording(message: types.Message):
    await bot.send_message(
        message.from_user.id,
        'Здесь нужно отобразить свободное время с привязкой к календарю.Хз как делать)'
    )


# @dp.message_handler(commands=['Режим_работы'])
async def time_opened(message: types.Message):
    await bot.send_message(
        message.from_user.id,
        'График работы'
    )


# @dp.message_handler(commands=['Контакты'])
async def contacts(message: types.Message):
    await bot.send_message(
        message.from_user.id,
        'Номер телефона, почта мб.'
    )


# @dp.message_handler(commands=['Мои_записи'])
async def my_recording(message: types.Message):
    await bot.send_message(
        message.from_user.id,
        'Сюда выводить записи. Если их нет отправлять смс. Нужно уведомление настроить если есть запись'
    )


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(commands_start, commands=['start', 'help'])
    dp.register_message_handler(list_services, text='Услуги')
    dp.register_message_handler(recording, text='Запись')
    dp.register_message_handler(time_opened, text='Режим работы')
    dp.register_message_handler(contacts, text='Контакты')
    dp.register_message_handler(my_recording, text='Мои записи')
