from fastapi import FastAPI
from routes import users
from db.database import engine
from db import models

app = FastAPI()

# Создаём таблицы при запуске
models.Base.metadata.create_all(bind=engine)

app.include_router(users.router)

@app.get("/")
def root():
    return {"message": "FastAPI с базой данных работает!"}