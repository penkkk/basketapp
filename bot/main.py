from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.filters import Command
from config import Config
import asyncio

bot = Bot(token=Config.BOT_TOKEN)
dp = Dispatcher()

# Хендлер на команду /start
@dp.message(Command("start"))
async def start_handler(message: Message):
    await message.answer("Привет! Бот работает!")

# Функция запуска бота
async def main():
    try:
        print("Бот запускается...")
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(main())
