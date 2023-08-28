"""
Создать веб-страницу для отображения списка пользователей. Приложение
должно использовать шаблонизатор Jinja для динамического формирования HTML
страницы.
Создайте модуль приложения и настройте сервер и маршрутизацию.
Создайте класс User с полями id, name, email и password.
Создайте список users для хранения пользователей.
Создайте HTML шаблон для отображения списка пользователей. Шаблон должен
содержать заголовок страницы, таблицу со списком пользователей и кнопку для
добавления нового пользователя.
Создайте маршрут для отображения списка пользователей (метод GET).
Реализуйте вывод списка пользователей через шаблонизатор Jinja.
"""
import pydantic
import uvicorn
from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")
users = []


class User(BaseModel):
    id_: int
    name: str
    email: pydantic.EmailStr
    password: pydantic.SecretStr


users.append(User(id_=1, name="Alex", email="eee@www.com", password="123"))
users.append(User(id_=2, name="Olga", email="ooo@www.com", password="123"))


@app.get('/users/', response_class=HTMLResponse)
async def all_users(request: Request):
    return templates.TemplateResponse("task6.html", {"request": request, "users": users})


@app.post('/user/add')
async def add_user(user: User):
    users.append(user)
    return {"user": user, "status": "added"}


if __name__ == "__main__":
    uvicorn.run("task_6:app", port=8000)
