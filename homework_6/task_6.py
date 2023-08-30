"""
Необходимо создать базу данных для интернет-магазина. База данных должна состоять из трех таблиц: товары,
заказы и пользователи. Таблица товары должна содержать информацию о доступных товарах, их описаниях и ценах.
Таблица пользователи должна содержать информацию о зарегистрированных пользователях магазина. Таблица заказы
должна содержать информацию о заказах, сделанных пользователями.
    ○ Таблица пользователей должна содержать следующие поля: id (PRIMARY KEY),
    имя, фамилия, адрес электронной почты и пароль.
    ○ Таблица товаров должна содержать следующие поля: id (PRIMARY KEY),
    название, описание и цена.
    ○ Таблица заказов должна содержать следующие поля: id (PRIMARY KEY), id
    пользователя (FOREIGN KEY), id товара (FOREIGN KEY), дата заказа и статус
    заказа.
Создайте модели pydantic для получения новых данных и возврата существующих в БД для каждой из трёх таблиц
(итого шесть моделей).
Реализуйте CRUD операции для каждой из таблиц через создание маршрутов, REST API (итого 15 маршрутов).
    ○ Чтение всех
    ○ Чтение одного
    ○ Запись
    ○ Изменение
    ○ Удаление
"""

import uvicorn
from fastapi import FastAPI
import databases
from typing import List
from datetime import datetime
from models import users, User, UserIn, goods, Goods, GoodsIn, orders, Order, OrderIn

DATABASE_URL = "sqlite:///mydatabase.db"
database = databases.Database(DATABASE_URL)

app = FastAPI(title="Homework_6")


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


@app.get("/")
async def home():
    return "Welcome to our shop!"


# ============== User ============================
@app.get("/users/", response_model=List[User])
async def read_all():
    query = users.select()
    return await database.fetch_all(query)


@app.get("/users/{user_id}", response_model=User)
async def read_one(user_id: int):
    query = users.select().where(users.c.id == user_id)
    return await database.fetch_one(query)


@app.post("/user/add", response_model=User)
async def create_user(user: UserIn):
    query = users.insert().values(name=user.name, surname=user.surname, email=user.email, password=user.password)
    last_record_id = await database.execute(query)
    return {**user.dict(), "id": last_record_id}


@app.put("/user/update/{user_id}", response_model=User)
async def update_user(user: UserIn, user_id: int):
    query = users.update().where(users.c.id == user_id).values(name=user.name, surname=user.surname, email=user.email,
                                                               password=user.password)
    await database.execute(query)
    return {**user.model_dump(), "id": user_id}


@app.delete("/user/delete/{user_id}")
async def delete_user(user_id: int):
    query = users.delete().where(users.c.id == user_id)
    await database.execute(query)
    return {"msg": f"User deleted {user_id}"}


# ============= Goods ===============================
@app.get("/goods/", response_model=List[Goods])
async def read_all():
    query = goods.select()
    return await database.fetch_all(query)



@app.get("/goods/{item_id}", response_model=Goods)
async def read_one(item_id: int):
    query = goods.select().where(goods.c.id == item_id)
    return await database.fetch_one(query)


@app.post("/goods/add", response_model=Goods)
async def create_item(item: GoodsIn):
    query = goods.insert().values(name=item.name, description=item.description, price=item.price)
    last_record_id = await database.execute(query)
    return {**item.dict(), "id": last_record_id}


@app.put("/goods/update/{item_id}", response_model=Goods)
async def update_item(item: UserIn, item_id: int):
    query = goods.update().where(goods.c.id == item_id).values(name=item.name, description=item.description,
                                                               price=item.price)
    await database.execute(query)
    return {**item.model_dump(), "id": item_id}


@app.delete("/goods/delete/{item_id}")
async def delete_item(item_id: int):
    query = goods.delete().where(goods.c.id == item_id)
    await database.execute(query)
    return {"msg": f"Item deleted {item_id}"}


# ============= Orders ===============================
@app.get("/orders/", response_model=List[Order])
async def read_all():
    query = orders.select()
    return await database.fetch_all(query)



@app.get("/orders/{order_id}", response_model=Order)
async def read_one(order_id: int):
    query = orders.select().where(orders.c.id == order_id)
    return await database.fetch_one(query)


@app.post("/orders/add", response_model=Order)
async def create_order(order: OrderIn):
    query = orders.insert().values(customer_id=orders.customer_id, item_id=order.item_id, order_date=datetime.now(), status=order.status)
    last_record_id = await database.execute(query)
    return {**order.dict(), "id": last_record_id}


@app.put("/orders/update/{order_id}", response_model=Order)
async def update_orders(order: OrderIn, order_id: int):
    query = orders.update().where(orders.c.id == order_id).values(customer_id=orders.customer_id, item_id=order.item_id, order_date=datetime.now(), status=order.status)
    await database.execute(query)
    return {**order.model_dump(), "id": order_id}


@app.delete("/orders/delete/{order_id}")
async def delete_order(order_id: int):
    query = orders.delete().where(orders.c.id == order_id)
    await database.execute(query)
    return {"msg": f"Item deleted {order_id}"}



if __name__ == "__main__":
    uvicorn.run("task_6:app", port=8000)
