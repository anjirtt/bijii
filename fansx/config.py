import os
from dotenv import load_dotenv

load_dotenv(".env")

MAX_BOT = int(os.getenv("MAX_BOT", "400"))

DEVS = list(map(int, os.getenv("DEVS", "8711726001").split()))

API_ID = int(os.getenv("API_ID", "31744107"))

API_HASH = os.getenv("API_HASH", "7e48044f6cca92da38d7e1bad87ad096")

BOT_TOKEN = os.getenv("BOT_TOKEN", "8648903246:AAEGypVK4WxL4vtOT3fMY47gVgSdYN3fsGY")

OWNER_ID = int(os.getenv("OWNER_ID", "8711726001"))

BLACKLIST_CHAT = list(map(int, os.getenv("BLACKLIST_CHAT", "-1003192483568").split()))

RMBG_API = os.getenv("RMBG_API", "f8N4KnJwDK2nbJ6wZ2D6tweg")

MONGO_URL = os.getenv("MONGO_URL", "mongodb+srv://danargntng34_db_user:LbTitJc30N2qJnRA@cluster0.zl4jybb.mongodb.net/?appName=Cluster0")

LOGS_MAKER_UBOT = int(os.getenv("LOGS_MAKER_UBOT", "-1003394338696"))
