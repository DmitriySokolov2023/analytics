from sqlalchemy import create_engine
import pandas as pd


def push_to_db(df):
  engine = create_engine("postgresql://metabase800:c[jkf800@analytics.shkola800.ru:5432/school800")
  try:
    df.to_sql("scor_az_2425", engine, schema="public",if_exists="replace", index=False)
    print("✅ Таблица создана и данные загружены")
  except ValueError as e:
        if 'already exists' in str(e):
            print("ℹ️ Таблица уже существует. Ничего не делаем.")
        else:
            print("❌ Ошибка:", e)
            raise
        
table = pd.read_excel('data/Scores_AZ.xlsx')
df = pd.DataFrame(table)
push_to_db(df)