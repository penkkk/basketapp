from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.filters import Command
from bot.config import Config
from bot.services.infobasket_api import InfoBasketAPI
from bot.handlers import routers
import asyncio
    
async def main():
    bot = Bot(token=Config.BOT_TOKEN)
    dp = Dispatcher()
    for router in routers:
        dp.include_router(router)
        
    print("Бот запущен")
    await dp.start_polling(bot)

    
if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Exit")
