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
# посмотреть доки: http://localhost:8000/docs
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


# передать данные о задаче (создать новую задачу)
@app.post("/tasks")
async def create_task(task: TaskModel):
    next_id = max(tasks, key=lambda x: x.id).id + 1
    next_task = Task(id=next_id, title=task.title, description=task.description, status=task.status)
    tasks.append(next_task)


# внести изменения в существующую задачу
@app.put("/tasks/{task_id}", response_model=Task)
async def change_task(task_id: int, task: TaskModel):
    update_task = [t for t in tasks if t.id == task_id]
    if not update_task:
        raise HTTPException(status_code=404, detail='Task not found')
    update_task[0].title = task.title
    update_task[0].description = task.description
    update_task[0].status = task.status
    return update_task[0]


# удалить задачу
@app.delete("/tasks/{task_id}")
async def delete_task(task_id: int):
    task = [task for task in tasks if task.id == task_id]
    if task:
        tasks.remove(task[0])
        return task_id
    raise HTTPException(status_code=404, detail='Task not found')
