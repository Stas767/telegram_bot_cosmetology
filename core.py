from aiogram import Bot
from aiogram.dispatcher import Dispatcher
# храним машину состояния в памяти
from aiogram.contrib.fsm_storage.memory import MemoryStorage


storage = MemoryStorage()

bot = Bot(token='5710965632:AAGXeseNKF_D-sIrxFL8scS3a3vlDnJ0SJ0')
dp = Dispatcher(bot, storage=storage)
