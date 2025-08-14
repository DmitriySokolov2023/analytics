"""
config.py
Хранит базовые настройки проекта
"""

import os
from dotenv import load_dotenv

# Загружаем переменные из .env
load_dotenv()

# Eljur API
TOKEN = os.getenv("token")
LOGIN = os.getenv("login")
PASSWORD =os.getenv("password")
DEVKEY = os.getenv("devkey")
VENDOR = os.getenv("vendor")
API_URL = "https://edu.gounn.ru/api"
API_PARAMS = f"devkey={DEVKEY}&login={LOGIN}&password={PASSWORD}&vendor={VENDOR}&token={TOKEN}"


# PostgreSQL
PG_USER = os.getenv("PG_USER")
PG_PASSWORD = os.getenv("PG_PASSWORD")
PG_HOST = os.getenv("PG_HOST", "localhost")
PG_PORT = os.getenv("PG_PORT", "5432")
PG_DATABASE = os.getenv("PG_DATABASE")

