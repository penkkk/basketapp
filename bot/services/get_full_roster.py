from bot.services.infobasket_api import InfoBasketAPI
from bot.config import Config


def full_roster():
    
    TEAM_ID = Config.TEAM_ID
    COMP_ID = Config.COMP_ID

    infobasket_api = InfoBasketAPI(TEAM_ID, COMP_ID)

    roster = infobasket_api.get_team_roster()
    players = roster.get("Players", [])
    full_roster = {}
    for player in players:
        person_info = player.get("PersonInfo", {})
        person_full_name_ru = person_info.get("PersonFullNameRu", "")
        person_id_roster = person_info.get("PersonID")
        full_roster[person_full_name_ru] = person_id_roster
    
    return full_roster
    