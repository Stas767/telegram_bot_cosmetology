from aiogram.utils import executor

from core import dp
from database import sqlite_db
from handlers import admin, client


async def on_startup(_):
    print('Бот вышел в онлайн')  # временный логинг
    sqlite_db.sql_start()

client.register_handlers_client(dp)
admin.register_handlers_admin(dp)

executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
