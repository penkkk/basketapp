from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from bot.services.get_full_roster import full_roster

async def inline_roster():
    keyboard = []

    for idx, player_name in enumerate(full_roster):
        keyboard.append([
            InlineKeyboardButton(
                text=player_name,
                callback_data=f"player:{idx}")])

    return InlineKeyboardMarkup(inline_keyboard=keyboard)
