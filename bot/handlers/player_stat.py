from aiogram import Router, types, F
from aiogram.types import Message
from aiogram.filters import Command
from bot.keyboards import inlinekeyboard

router = Router()

@router.message(Command("statplayer"))
async def stat_player_handler(message: Message):
    await message.answer("Выбери игрока", 
                         reply_markup= await inlinekeyboard.inline_roster())

@router.message(F.text == "📈 Cтатистика игрока")
async def stat_player_from_button(message: Message):
    await stat_player_handler(message)
