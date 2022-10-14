import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "")
BOT_TOKEN = getenv("BOT_TOKEN", "")
BOT_NAME = getenv("BOT_NAME", "")
API_ID = int(getenv("API_ID", ""))
API_HASH = getenv("API_HASH", "")
OWNER_NAME = getenv("OWNER_NAME", "")
OWNER_USERNAME = getenv("OWNER_USERNAME", "")
ALIVE_NAME = getenv("ALIVE_NAME", "")
BOT_USERNAME = getenv("BOT_USERNAME")
OWNER_ID = getenv("OWNER_ID")
ASSISTANT_NAME = getenv("ASSISTANT_NAME")
GROUP_SUPPORT = getenv("GROUP_SUPPORT")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1253258650").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://te.legra.ph/file/7e5b79d224638c0d1a38f.jpg")
START_PIC = getenv("START_PIC", "https://te.legra.ph/file/c4ffad012292d4b4cb6bc.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/DOMINATOR-XD/NIXA-MUSIC-BOT")
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/c4ffad012292d4b4cb6bc.jpg")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/c4ffad012292d4b4cb6bc.jpg")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/c4ffad012292d4b4cb6bc.jpg")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/c4ffad012292d4b4cb6bc.jpg")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/c4ffad012292d4b4cb6bc.jpg")
IMG_6 = getenv("IMG_6", "https://te.legra.ph/file/c4ffad012292d4b4cb6bc.jpg")
