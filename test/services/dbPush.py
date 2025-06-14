import pandas as pd
from sqlalchemy import create_engine
from urllib.parse import quote_plus

def push_in_db():
    
    engine = create_engine("postgresql://sokolov:SySHjAoLXO3SxLZa0WNiTRQqtwhQxz2W@dpg-d13h9v3e5dus73eoofug-a.frankfurt-postgres.render.com/analytics_ycdp")

    df = pd.DataFrame({
    'student_id': [1, 2],
    'name': ['Alice', 'Bob'],
    'score': [95, 88]
})
    try:
        # Пытаемся создать таблицу и вставить данные
        df.to_sql('students_scores', engine, if_exists='fail', index=False, schema='analytics')
        print("✅ Таблица создана и данные загружены")
    except ValueError as e:
        if 'already exists' in str(e):
            print("ℹ️ Таблица уже существует. Ничего не делаем.")
        else:
            print("❌ Ошибка:", e)
            raise