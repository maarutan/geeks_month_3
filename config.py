from aiogram import Bot, Dispatcher  
from decouple import config  


token = config("TOKEN2")
bot = Bot(token=token)
dp = Dispatcher(bot)
