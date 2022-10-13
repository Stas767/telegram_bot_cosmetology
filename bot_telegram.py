from aiogram.utils import executor
from core import dp
from handlers import client


async def on_startup(_):
    print('Бот вышел в онлайн') # временный логинг

client.register_handlers_client(dp) 

executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
