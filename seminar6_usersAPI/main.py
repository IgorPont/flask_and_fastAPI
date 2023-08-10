"""
Разработать API для управления списком пользователей с
использованием базы данных SQLite.
"""

from fastapi import FastAPI, Query, HTTPException
from database import db
import users
import uvicorn

app = FastAPI(title="Seminar 6")

app.include_router(users.router, tags=["Users"])


@app.on_event("startup")
async def startup():
    await db.connect()


@app.on_event("shutdown")
async def shutdown():
    await db.disconnect()


if __name__ == '__main__':
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
