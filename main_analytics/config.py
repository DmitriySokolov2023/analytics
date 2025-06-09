"""
config.py
Хранит базовые настройки проекта
"""

import os
from dotenv import load_dotenv

# Загружаем переменные из .env
load_dotenv()

# Eljur API
ELJUR_API_URL = "https://api.eljur.ru/api/getassessments"
ELJUR_TOKEN = os.getenv("ELJUR_TOKEN")

# PostgreSQL
PG_USER = os.getenv("PG_USER")
PG_PASSWORD = os.getenv("PG_PASSWORD")
PG_HOST = os.getenv("PG_HOST", "localhost")
PG_PORT = os.getenv("PG_PORT", "5432")
PG_DATABASE = os.getenv("PG_DATABASE")

# Прочее
DEFAULT_STUDENTS = ["123", "124", "125"]  # Пример ID учеников
DEFAULT_DATE_RANGE = "20250601-20250607"
