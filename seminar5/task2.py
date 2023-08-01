"""
Создать API для получения списка фильмов по жанру. Приложение должно иметь возможность получать список фильмов по
заданному жанру.
Создайте модуль приложения и настройте сервер и маршрутизацию.
Создайте класс Movie с полями id, title, description и genre.
Создайте список movies для хранения фильмов.
Создайте маршрут для получения списка фильмов по жанру (метод GET).
Реализуйте валидацию данных запроса и ответа.
"""

import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

# запуск: uvicorn task2:app --reload
# посмотреть доки: http://localhost:8000/docs
app = FastAPI()


class Genre(BaseModel):
    id: int
    name: str


class Movie(BaseModel):
    id: int
    title: str
    description: str
    genre: Genre


movies = [
    Movie(id=i, title=f'title {i}', description=f'description {i}', genre=Genre(id=i % 3, name=f'gen {(i % 3) ** 2}'))
    for i in range(1, 6)
]


# запрос всех фильмов (либо фильмов по жанру id)
@app.get('/movies', response_model=list[Movie])
async def get_movies(gen_id: int = None):
    if not gen_id:
        return movies
    movie_list = [m for m in movies if m.genre.id == gen_id]
    return movie_list


if __name__ == '__main__':
    # для запуска через run PyCharm
    uvicorn.run(
        "task2.app",
        host="127.0.0.1",
        port=8000,
        reload=True
    )
