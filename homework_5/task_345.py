"""
Создать API для добавления нового пользователя в базу данных. Приложение должно иметь возможность принимать POST запросы
с данными нового пользователя и сохранять их в базу данных.
Создайте модуль приложения и настройте сервер и маршрутизацию.
Создайте класс User с полями id, name, email и password.
Создайте список users для хранения пользователей.
Создайте маршрут для добавления нового пользователя (метод POST).
Реализуйте валидацию данных запроса и ответа.
"""
import pydantic
import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()
users = []


class User(BaseModel):
    id_: int
    name: str
    email: pydantic.EmailStr
    password: pydantic.SecretStr


users.append(User(id_=1, name="Alex", email="eee@www.com", password="123"))
users.append(User(id_=2, name="Olga", email="ooo@www.com", password="123"))


@app.get('/users/')
async def all_users():
    return {'users': users}


@app.post('/user/add')
async def add_user(user: User):
    users.append(user)
    return {"user": user, "status": "added"}


@app.put('/user/update/{user_id}')
async def update_user(user_id: int, user: User):
    for u in users:
        if u.id_ == user_id:
            u.name = user.name
            u.email = user.email
            u.password = user.password
            return {"user": user, "status": "updated"}
    return HTTPException(404, 'Task not found')


@app.delete('/user/delete/{user_id}')
async def delete_user(user_id: int):
    for u in users:
        if u.id_ == user_id:
            users.remove(u)
            return {"status": "success"}
    return HTTPException(404, 'Task not found')

if __name__ == "__main__":
    uvicorn.run("sem345:app", port=8000)