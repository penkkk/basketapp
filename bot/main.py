from aiogram import Bot, Dispatcher, types
from aiohttp_socks import ProxyConnector
from bot.config import Config
from bot.handlers import routers
import asyncio
    
async def main():
    
    connector = ProxyConnector.from_url(Config.PROXY_URL)
    bot = Bot(token=Config.BOT_TOKEN, proxy=connector)
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
