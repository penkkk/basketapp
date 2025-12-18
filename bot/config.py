import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    BOT_TOKEN = os.getenv("BOT_TOKEN")
    COMP_ID = int(os.getenv("COMP_ID"))
    TEAM_ID = int(os.getenv("TEAM_ID"))
    HTTP5_URL = os.getenv("HTTP5_URL")
