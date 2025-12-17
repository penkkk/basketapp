from aiogram import Router, types
from aiogram.types import Message
from aiogram.filters import Command

router = Router()

@router.message(Command("help"))
async def help_handler(message: Message):
    await message.answer(
        "/start - приветствие\n"
        "/help - помощь по командам\n"
        "/team - информации по команде\n"
        )
