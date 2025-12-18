from aiogram import Router, types, F
from aiogram.types import Message
from aiogram.filters import Command
from bot.keyboards import replykeyboard

router = Router()

@router.message(Command("start"))
async def start_handler(message: Message):
    await message.answer("Привет! Это твой баскетбольный помощник", 
                         reply_markup=replykeyboard.main)

@router.message(F.text == "↩️ Назад")
async def start_from_back_button(message: Message):
    await start_handler(message)    
