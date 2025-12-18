import requests

class InfoBasketAPI:
    BASE_URL = "https://reg.infobasket.su/Widget"

    def __init__(self, team_id: int, comp_id: int):
        self.team_id = team_id
        self.comp_id = comp_id

    def get_team_roster(self):
        url = f"{self.BASE_URL}/TeamRoster/{self.team_id}?compId={self.comp_id}&format=json&lang=ru"
        r = requests.get(url)
        return r.json() if r.status_code == 200 else None

    def get_team_schedule(self):
        url = f"{self.BASE_URL}/TeamGames/{self.team_id}?compId={self.comp_id}&format=json&lang=ru"
        r = requests.get(url)
        return r.json() if r.status_code == 200 else None
    
    def get_team_stat(self):
        url = f"{self.BASE_URL}/TeamStats/{self.team_id}?compId={self.comp_id}&format=json&lang=ru"
        r = requests.get(url)
        return r.json() if r.status_code == 200 else None
