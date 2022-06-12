from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

API_ID = int(getenv("API_ID", "18528144"))
API_HASH = getenv("API_HASH", "3d78673406ea6650f61bee392e974171")
BOT_TOKEN = getenv("BOT_TOKEN", None)
BOT_NAME = getenv("BOT_NAME","STARMUSIC")
BOT_USERNAME = getenv("BOT_USERNAME", "STAR_X_MUICBOT")
OWNER_USERNAME = getenv("OWNER_USERNAME", "STAROF_WORLD")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "decant_club")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))
START_IMG = getenv("START_IMG", "https://te.legra.ph/file/125d5d3636db066a35df3.jpg")
PING_IMG = getenv("PING_IMG", "https://te.legra.ph/file/125d5d3636db066a35df3.jpg")
SESSION_NAME = getenv("SESSION_NAME", None)
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "• / ! ^ .").split())
PMPERMIT = getenv("PMPERMIT", "ENABLE")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5022574807").split()))
