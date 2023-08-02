"""
Создать RESTful API для управления списком задач. Приложение должно использовать FastAPI и поддерживать следующие
функции:
○ Получение списка всех задач.
○ Получение информации о задаче по её ID.
○ Добавление новой задачи.
○ Обновление информации о задаче по её ID.
○ Удаление задачи по её ID.
Каждая задача должна содержать следующие поля: ID (целое число),
Название (строка), Описание (строка), Статус (строка): 'todo', 'in progress', 'done'.
"""

import enum
import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


# Для множественного статуса
class Status(enum.Enum):
    todo = 'todo'
    in_progress = 'in progress'
    done = 'done'


class Task(BaseModel):
    id: int
    title: str
    description: str
    status: Status


class TaskInput(BaseModel):
    title: str
    description: str
    status: Status


tasks = []

app = FastAPI()


@app.get("/tasks", response_model=list[Task])
def get_tasks():
    return tasks


@app.post("/tasks", response_model=list[Task])
def new_task(task: TaskInput):
    task = Task(
        id=len(tasks) + 1,
        title=task.title,
        description=task.description,
        status=task.status
    )
    tasks.append(task)
    return tasks


@app.put("/tasks/{task_id}", response_model=TaskInput)
def edit_task(task_id: int, new_task: Task):
    for task in tasks:
        if task.id == task_id:
            task.title = new_task.title
            task.description = new_task.description
            task.status = new_task.status
            return task
    raise HTTPException(status_code=404, detail="Task not found")


@app.delete("/tasks/{task_id}", response_model=str)
def delete_task(task_id: int):
    for task in tasks:
        if task.id == task_id:
            tasks.remove(task)
            return "task was deleted"
    raise HTTPException(status_code=404, detail="Task not found")


if __name__ == '__main__':
    uvicorn.run(
        "task1:app",
        host="127.0.0.1",
        port=8000,
        reload=True
    )
