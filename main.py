import asyncio
import random
from aiogram import Bot, types, Dispatcher, Router
from aiogram.types import Message
from aiogram.filters import Command
from dotenv import dotenv_values

from handlers.start import start_router
from handlers.complaint import questions_router
token = dotenv_values('.env')['BOT_TOKEN']
bot = Bot(token=token)
dp = Dispatcher()
router = Router()
dp.include_router(router)



async def main():
    dp.include_router(start_router)
    dp.include_router(questions_router)
    # Запуск бота
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())