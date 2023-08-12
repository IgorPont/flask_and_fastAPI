"""
Необходимо создать базу данных для интернет-магазина.
База данных должна состоять из трёх таблиц: товары, заказы и пользователи.
- Таблица «Товары» должна содержать информацию о доступных товарах, их описаниях и ценах.
- Таблица «Заказы» должна содержать информацию о заказах, сделанных пользователями.
- Таблица «Пользователи» должна содержать информацию о зарегистрированных пользователях магазина.
• Таблица пользователей должна содержать следующие поля: id (PRIMARY KEY), имя, фамилия, адрес электронной почты и
пароль.
• Таблица заказов должна содержать следующие поля: id (PRIMARY KEY), id пользователя (FOREIGN KEY), id товара
(FOREIGN KEY), дата заказа и статус заказа.
• Таблица товаров должна содержать следующие поля: id (PRIMARY KEY), название, описание и цена.

Необходимо создать модели pydantic для получения новых данных и возврата существующих в БД для каждой из трёх таблиц.
Реализовать CRUD операции для каждой из таблиц через создание маршрутов, REST API.
"""

from fastapi import FastAPI
from database import db
from homework6_OnlineStore.routers import users, products, orders
import uvicorn

app = FastAPI(title="Online store")

app.include_router(users.router, tags=["Users"])
app.include_router(products.router, tags=["Products"])
app.include_router(orders.router, tags=["Orders"])


@app.on_event("startup")
async def startup():
    await db.connect()


@app.on_event("shutdown")
async def shutdown():
    await db.disconnect()


if __name__ == '__main__':
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
