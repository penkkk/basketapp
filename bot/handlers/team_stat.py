from aiogram import Router, types, F
from aiogram.types import Message
from aiogram.filters import Command
from bot.services.infobasket_api import InfoBasketAPI
from bot.config import Config


TEAM_ID = Config.TEAM_ID
COMP_ID = Config.COMP_ID
infobasket_api = InfoBasketAPI(TEAM_ID, COMP_ID)

router = Router()

@router.message(Command("statteam"))
async def stat_team_handler(message: Message):
    
    stat = infobasket_api.get_team_stat()
    
    if stat is None:
        await message.answer("Не удалось найти состав команды")
        return
    
    game_count = stat.get("GameCount")
    shots1 = stat.get("Shots1")
    shots2 = stat.get("Shots2")
    shots3 = stat.get("Shots3")
    shot_1_percent = stat.get("Shot1Percent")
    shot_2_percent = stat.get("Shot2Percent")
    shot_3_percent = stat.get("Shot3Percent")
    avg_points = stat.get("AvgPoints")
    avg_blocks = stat.get("AvgBlocks")
    avg_def_rebound = stat.get("AvgDefRebound")
    avg_off_rebound = stat.get("AvgOffRebound")
    avg_steal = stat.get("AvgSteal")
    avg_turnover = stat.get("AvgTurnover")
    
    text = f"""
    📊 Статистика команды:
    
    
    🧮 Количество игр: {game_count}
    
    1️⃣ Штрафные броски: {shots1} ({shot_1_percent} %)
    
    2️⃣ Двухочковые броски: {shots2} ({shot_2_percent} %)
    
    3️⃣ Трехочковые броски: {shots3} ({shot_3_percent} %)
    
    ↔️ Среднее количество очков за игру: {avg_points}
    
    🔒 Блокшоты за игру: {avg_blocks}
    
    🔀 Подборы на своем щите за игру: {avg_def_rebound}
    
    🔀 Подборы на чужом щите за игру: {avg_off_rebound}
    
    ⛹️‍♂️ Перехваты за игру: {avg_steal}
    
    🤦🏾‍♀️ Потери за игру: {avg_turnover}
    """
        
    await message.answer(text)
    
@router.message(F.text == "📈 Статистика команды")
async def stat_team_from_button(message: Message):
    await stat_team_handler(message)
