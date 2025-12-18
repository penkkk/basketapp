from aiogram import Router, types, F
from aiogram.types import Message
from aiogram.filters import Command
from bot.services.infobasket_api import InfoBasketAPI
from bot.config import Config


TEAM_ID = Config.TEAM_ID
COMP_ID = Config.COMP_ID
infobasket_api = InfoBasketAPI(TEAM_ID, COMP_ID)

router = Router()

@router.message(Command("team"))
async def team_handler(message: Message):
    
    roster = infobasket_api.get_team_roster()
    players = roster.get("Players", [])
    
    if roster is None:
        await message.answer("Не удалось найти состав команды")
        return
    
    text = "📋 Состав команды: \n\n"
    
    for number, player in enumerate(players):
        person_info = player.get("PersonInfo", {})
        person_full_name_ru = person_info.get("PersonFullNameRu", "")
        player_number = player.get("PlayerNumber")
        height = player.get("Height")
        position = player.get("Position")
        weight = player.get("Weight")
        text += f"{player_number} - {person_full_name_ru}\nПозиция: {position}\nРост: {height}, Вес: {weight}\n---------------------------\n"
        
    await message.answer(text)

@router.message(F.text == "📋 Состав команды")
async def team_from_button(message: Message):
    await team_handler(message)
