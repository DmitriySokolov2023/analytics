"""
config.py
Хранит базовые настройки проекта
"""

import os
from dotenv import load_dotenv

# Загружаем переменные из .env
load_dotenv()

# Eljur API
API_URL = "https://edu.gounn.ru/api/"
TOKEN = os.getenv("token")

# PostgreSQL
PG_USER = os.getenv("PG_USER")
PG_PASSWORD = os.getenv("PG_PASSWORD")
PG_HOST = os.getenv("PG_HOST", "localhost")
PG_PORT = os.getenv("PG_PORT", "5432")
PG_DATABASE = os.getenv("PG_DATABASE")

