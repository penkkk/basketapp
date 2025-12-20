from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from bot.services.get_full_roster import full_roster

async def inline_roster():
    keyboard = []

    for name, id in full_roster().items():
        keyboard.append([
            InlineKeyboardButton(
                text=name,
                callback_data=f"player:{id}")])

    return InlineKeyboardMarkup(inline_keyboard=keyboard)
