from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.filters import Command
from bot.config import Config
from bot.services.infobaket_api import InfoBasketAPI
import asyncio

bot = Bot(token=Config.BOT_TOKEN)
team_id = Config.TEAM_ID
comp_id = Config.COMP_ID
dp = Dispatcher()


# Хендлер на команду /start
@dp.message(Command("start"))
async def start_handler(message: Message):
    await message.answer("Привет! Бот работает!")

@dp.message(Command("help"))
async def help_handler(message: Message):
    await message.answer(
        "/start - приветствие\n"
        "/help - помощь по командам\n"
        "/team - информации по команде\n"
        )

# Функция запуска бота
async def main():
    try:
        print("Бот запускается...")
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(main())
