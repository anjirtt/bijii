import os
from dotenv import load_dotenv

load_dotenv(".env")

MAX_BOT = int(os.getenv("MAX_BOT", "400"))

DEVS = list(map(int, os.getenv("DEVS", "7837317427").split()))

API_ID = int(os.getenv("API_ID", "35549269"))

API_HASH = os.getenv("API_HASH", "c141efa27296c0c068172c34d847a758")

BOT_TOKEN = os.getenv("BOT_TOKEN", "8537047218:AAGDJQz8cKmVJDa7_MXjmTrZtZUGCQCXo9w")

OWNER_ID = int(os.getenv("OWNER_ID", "7837317427"))

BLACKLIST_CHAT = list(map(int, os.getenv("BLACKLIST_CHAT", "-1003192483568").split()))

RMBG_API = os.getenv("RMBG_API", "f8N4KnJwDK2nbJ6wZ2D6tweg")

MONGO_URL = os.getenv("MONGO_URL", "mongodb+srv://danargntng34_db_user:LbTitJc30N2qJnRA@cluster0.zl4jybb.mongodb.net/?appName=Cluster0")

LOGS_MAKER_UBOT = int(os.getenv("LOGS_MAKER_UBOT", "-1003411535752"))
