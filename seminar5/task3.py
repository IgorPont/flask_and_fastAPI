"""
Создать API для добавления нового пользователя в базу данных. Приложение должно иметь возможность принимать POST
запросы с данными нового пользователя и сохранять их в базу данных.
Создайте модуль приложения и настройте сервер и маршрутизацию.
Создайте класс User с полями id, name, email и password.
Создайте список users для хранения пользователей.
Создайте маршрут для добавления нового пользователя (метод POST).
Реализуйте валидацию данных запроса и ответа.
"""
import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr, Field
from typing import Optional

# запуск: uvicorn task3:app --reload
# посмотреть доки: http://localhost:8000/docs
app = FastAPI()


class User(BaseModel):
    id: int
    name: str
    email: EmailStr
    password: str


class UserDump(BaseModel):
    id: int
    name: str
    # три точки указывает, что обязателен для заполнения и в него может попасть объект объект любого типа
    # валидация пароля мин 8 символов, все символы и спецзнаки
    email: EmailStr = Field(..., description='Email address of the users')
    password: str = Field(..., min_length=8,
                          # regex=r'^.*(?=.{8,})(?=.*[a-zA-Z])(?=.*\d)(?=.*[!#$%&? "]).*$',
                          description='Password of the user')


users = []


# Параметр 'summery' в docs делает пояснения к эндпоинту, параметр 'tags' объединяет эндпоинты в группы
# показать всех пользователей
@app.get('/users', response_model=list[User], summary='Вывести всех пользователей', tags=["Пользователи"])
async def get_users():
    return users


# добавить нового пользователя
@app.post('/user_add', summary='Добавить пользователя', tags=["Пользователи"])
async def add_user(new_user: UserDump):
    new_id = 1
    if users:
        new_id = max(users, key=lambda x: x.id).id + 1
    users.append(
        User(id=new_id,
             name=new_user.name,
             email=new_user.email,
             password=new_user.password)
    )


# обновление данных о пользователе
@app.put('/user_change', response_model=User, summary='Обновить данные о пользователе', tags=["Пользователи"])
async def change_user(user: UserDump, user_id: int):
    upd_user = [u for u in users if u.id == user_id]
    if not upd_user:
        raise HTTPException(status_code=404, detail='User not found')
    upd_user[0] = user.name
    upd_user[0] = user.email
    upd_user[0] = user.password
    return upd_user[0]


# удалить пользователя
@app.delete('/user_del', response_model=User, summary='Удалить пользователя', tags=["Пользователи"])
async def delete_user(user_id: int):
    del_user = [u for u in users if u.id == user_id]
    if not del_user:
        raise HTTPException(status_code=404, detail='User not found')
    users.remove(del_user[0])
    return del_user[0]
