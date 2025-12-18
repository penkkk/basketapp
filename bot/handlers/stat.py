from aiogram import Router, types, F
from aiogram.types import Message
from aiogram.filters import Command
from bot.keyboards import replykeyboard

router = Router()

@router.message(Command("stat"))
async def stat_handler(message: Message):
    await message.answer("Выбери чью статистику ты хочешь посмотерть", 
                         reply_markup=replykeyboard.stat)

@router.message(F.text == "📊 Статистика")
async def stat_from_button(message: Message):
    await stat_handler(message)
