import pandas as pd
from sqlalchemy import create_engine
from urllib.parse import quote_plus

def push_in_db(df):

    engine = create_engine("postgresql://metabase800:c[jkf800@analytics.shkola800.ru:5432/school800")


    try:
        df.to_sql("student_scores_test_sokolov", engine,schema='public', if_exists="replace", index=False)
        print("✅ Таблица создана и данные загружены")
    except ValueError as e:
        if 'already exists' in str(e):
            print("ℹ️ Таблица уже существует. Ничего не делаем.")
        else:
            print("❌ Ошибка:", e)
            raise