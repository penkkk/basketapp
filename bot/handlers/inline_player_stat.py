from aiogram import Router, F
from aiogram.types import CallbackQuery
from bot.services.get_full_roster import full_roster
from .get_player_stats import get_player_stat
from bot.keyboards.inlinekeyboard import inline_roster

router = Router()

@router.callback_query(F.data.startswith("player:"))
async def player_stat_callback(callback: CallbackQuery):
    person_id = int(callback.data.split(":")[1])
    
    stats = await get_player_stat(person_id=person_id)
    
    await callback.message.edit_text(f"{stats}", reply_markup= await inline_roster())
    await callback.answer()
