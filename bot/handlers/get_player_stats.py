from bot.services.infobasket_api import InfoBasketAPI
from bot.config import Config

TEAM_ID = Config.TEAM_ID
COMP_ID = Config.COMP_ID

api = InfoBasketAPI(TEAM_ID, COMP_ID)

async def get_player_stat(person_id: int):
    data = api.get_team_stat()

    if not data:
        return "❌ Не удалось получить статистику игрока"

    players = data.get("Players", [])

    for player in players:
        if player.get("PersonID") != person_id:
            continue

        person_info = player.get("PersonInfo", {})
        name = person_info.get("PersonFullNameRu", "Игрок")

        return (
            f"📊 Статистика игрока: {name}\n\n"
            f"1️⃣ Штрафные: {player.get('Shots1')} ({player.get('Shot1Percent')})\n"
            f"2️⃣ Двухочковые: {player.get('Shots2')} ({player.get('Shot2Percent')})\n"
            f"3️⃣ Трёхочковые: {player.get('Shots3')} ({player.get('Shot3Percent')})\n\n"
        )

    return "❌ Статистика игрока не найдена"
