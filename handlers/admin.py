from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

from core import bot, dp


ID_ADMIN = (824803853, 251881124)


class FSMAdmin(StatesGroup):
    title = State()
    description = State()
    photo = State()
    recommend = State()


async def access_check(message: types.Message):
    """Проверка доступа и вывод меню администратора."""

    if message.from_user.id in ID_ADMIN:
        await bot.send_message(
            message.from_user.id,
            'Добро пожаловать в админ-панель. Что будем делать?'
        )

# Начало диалога и загрузка пунка меню
# @dp.message_handler(commands='Добавить', state=None)


async def fsm_start(message: types.Message):
    if message.from_user.id in ID_ADMIN:
        await FSMAdmin.title.set()
        await bot.send_message(
            message.from_user.id,
            'ОК. Введите название услуги'
        )


# Ловим первый ответ и пишем в словарь
# @dp.message_handler(state=FSMAdmin.title)
async def load_title(message: types.Message, state: FSMContext):
    if message.from_user.id in ID_ADMIN:
        async with state.proxy() as data:
            data['title'] = message.text
        await FSMAdmin.next()
        await bot.send_message(
            message.from_user.id,
            'ОК. Опишите услугу.'
        )


# Ловим второй ответ и пишем в словарь
# @dp.message_handler(state=FSMAdmin.description)
async def load_description(message: types.Message, state: FSMContext):
    if message.from_user.id in ID_ADMIN:
        async with state.proxy() as data:
            data['description'] = message.text
        await FSMAdmin.next()
        await bot.send_message(
            message.from_user.id,
            'ОК. Загрузите фото.'
        )


# Ловим третий ответ и пишем в словарь
# @dp.message_handler(content_types='photo', state=FSMAdmin.photo)
async def load_photo(message: types.Message, state: FSMContext):
    if message.from_user.id in ID_ADMIN:
        async with state.proxy() as data:
            data['photo'] = message.photo[0].file_id
        await FSMAdmin.next()
        await bot.send_message(
            message.from_user.id,
            'ОК. Напиши рекомендации.'
        )


# Ловим последний ответ и пишем в словарь
# @dp.message_handler(state=FSMAdmin.recommend)
async def load_recommend(message: types.Message, state: FSMContext):
    if message.from_user.id in ID_ADMIN:
        async with state.proxy() as data:
            data['recommend'] = message.text

        async with state.proxy() as data:
            await bot.send_message(
                message.from_user.id,
                str(data)
            )
        await state.finish()


async def cancel_fsm(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if message.from_user.id in ID_ADMIN:
        if current_state is None:
            return
        await state.finish()
        await bot.send_message(
            message.from_user.id,
            'ОК. Выполнил отмену.'
        )


def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(
        fsm_start, state=None,
        text='Добавить новую услугу'
    )
    dp.register_message_handler(load_title, state=FSMAdmin.title)
    dp.register_message_handler(load_description, state=FSMAdmin.description)
    dp.register_message_handler(
        load_photo, content_types='photo',
        state=FSMAdmin.photo
    )
    dp.register_message_handler(load_recommend, state=FSMAdmin.recommend)
    dp.register_message_handler(cancel_fsm, text='Отмена', state='*')
    dp.register_message_handler(access_check, text='Админ')
