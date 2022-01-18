import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME", "Video Stream")
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
OWNER_NAME = getenv("OWNER_NAME", "UU_O_M_AR")
ALIVE_NAME = getenv("ALIVE_NAME", "𝐆𝐇𝐎𝐒𝐓 𝙓⃟🇫🇮™𓆩𝐎𝐒𝐇𝐀𓆪⸙ꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋ")
BOT_USERNAME = getenv("BOT_USERNAME", "MAGY1_MUSIC1_BOT")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "cleo_invida")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "osha36")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "GH_OS_T_M1")
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/3446396d5dbc85ad4ab9f.mp4")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/MostafaShalaby1")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/3446396d5dbc85ad4ab9f.mp4")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/3446396d5dbc85ad4ab9f.mp4")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/3446396d5dbc85ad4ab9f.mp4")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/3446396d5dbc85ad4ab9f.mp4")
