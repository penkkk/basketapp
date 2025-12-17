from aiogram import Router, types
from aiogram.types import Message
from aiogram.filters import Command
from bot.keyboards import replykeyboard

router = Router()

@router.message(Command("start"))
async def start_handler(message: Message):
    await message.answer("Привет! Это твой баскетбольный помощник", 
                         reply_markup=replykeyboard.main)
    