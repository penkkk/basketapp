from aiogram import Bot, Dispatcher, types
from bot.config import Config
from aiogram.client.session.aiohttp import AiohttpSession
from bot.handlers import routers
import asyncio
    
async def main():
    session = AiohttpSession(proxy=Config.HTTP5_URL)
    bot = Bot(token=Config.BOT_TOKEN, session=session)
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
