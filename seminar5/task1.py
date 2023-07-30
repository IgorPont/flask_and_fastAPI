"""
Создать API для управления списком задач. Приложение должно иметь
возможность создавать, обновлять, удалять и получать список задач.
Создайте модуль приложения и настройте сервер и маршрутизацию.
Создайте класс Task с полями id, title, description и status.
Создайте список tasks для хранения задач.
Создайте маршрут для получения списка задач (метод GET).
Создайте маршрут для создания новой задачи (метод POST).
Создайте маршрут для обновления задачи (метод PUT).
Создайте маршрут для удаления задачи (метод DELETE).
Реализуйте валидацию данных запроса и ответа.
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

# запуск: uvicorn task1:app --reload
app = FastAPI()


class Task(BaseModel):
    id: int
    title: str
    description: Optional[str]
    status: bool


class TaskModel(BaseModel):
    title: str
    description: Optional[str]
    status: bool


tasks = list()
tasks.append(Task(id=1, title='Title', description=None, status=False))


# получить все задачи (метод GET)
@app.get("/tasks", response_model=list[Task])
async def get_tasks():
    return tasks


# получить одну задачу (метод GET)
@app.get("/tasks/{task_id}", response_model=Task)
async def get_task_by_id(task_id: int):
    task = [task for task in tasks if task.id == task_id]
    if task:
        return task[0]
    raise HTTPException(status_code=404, detail='Task not found')


# передать данные о задаче (создать задачу)
@app.post("/tasks")
async def create_task(task: TaskModel):
# 0:49
