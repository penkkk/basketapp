from aiogram import Router, types
from aiogram.types import Message
from aiogram.filters import Command
from bot.services.infobasket_api import InfoBasketAPI
from bot.config import Config


TEAM_ID = Config.TEAM_ID
COMP_ID = Config.COMP_ID
infobasket_api = InfoBasketAPI(TEAM_ID, COMP_ID)

router = Router()

@router.message(Command("nextgame"))
async def next_game(message: Message):
    roster = infobasket_api.get_team_schedule()
    
    if roster is None:
        await message.answer("Не удалось найти предстоящие игры")
        return
    
    text = "Предстоящие встречи: \n\n"
    number = 0
    
    for match in roster:
        game_status = match.get("GameStatus")
        if game_status == 0:
            number += 1
            team_A = match.get("ShortTeamNameAru")
            team_B = match.get("ShortTeamNameBru")
            date_time = match.get("DisplayDateTimeMsk")
            text += f"{number}. {team_A} VS {team_B} | {date_time}\n\n"
    await message.answer(text)

