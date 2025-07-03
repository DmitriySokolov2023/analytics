import psycopg2
from psycopg2 import sql

def get_db_connection():
    try:
        conn = psycopg2.connect(
            dbname='school800',
            user='metabase800',
            password='c[jkf800',
            host='analytics.shkola800.ru'
        )
        return conn
    except psycopg2.OperationalError as e:
        print("Ошибка подключения к базе данных:", e)
        return None

def fetch_from_db(query, params=None):
    try:
        with get_db_connection() as conn, conn.cursor() as cursor:
            cursor.execute(query, params or ())
            return cursor.fetchall()
    except psycopg2.DatabaseError as e:
        print("Ошибка выполнения SQL-запроса:", e)
        return None

def push_to_db(query, data=None):
    try:
        with get_db_connection() as conn, conn.cursor() as cursor:
            cursor.execute(query, data or ())
            conn.commit()
            return True
    except psycopg2.DatabaseError as e:
        print("Ошибка выполнения SQL-запроса:", e)
        conn.rollback()
        return False

def push_many_to_db(query, data_list):
    try:
        with get_db_connection() as conn, conn.cursor() as cursor:
            cursor.executemany(query, data_list)
            conn.commit()
            return cursor.rowcount
    except psycopg2.DatabaseError as e:
        print("Ошибка выполнения SQL-запроса:", e)
        conn.rollback()
        return 0

def create_table(create_table_query):
    try:
        with get_db_connection() as conn, conn.cursor() as cursor:
            cursor.execute(create_table_query)
            conn.commit()
            print("Таблица успешно создана или уже существует")
    except psycopg2.DatabaseError as e:
        print("Ошибка выполнения SQL-запроса:", e)
        return None
    
create_table(
    """
    CREATE TABLE IF NOT EXISTS public.test_sokolov(
        id text,
        student_id INTEGER NOT NULL,
        student_name VARCHAR(100) NOT NULL,
        class_id INTEGER,
        subject VARCHAR(50),
        assessment_date DATE,
        score INTEGER,
        teacher_comment TEXT
    )
    """
)