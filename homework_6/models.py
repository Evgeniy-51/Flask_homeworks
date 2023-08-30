import sqlalchemy
from pydantic import BaseModel, Field
from datetime import datetime
from sqlalchemy import DateTime

DATABASE_URL = "sqlite:///mydatabase.db"
metadata = sqlalchemy.MetaData()


users = sqlalchemy.Table(
    "users", metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String(32)),
    sqlalchemy.Column("surname", sqlalchemy.String(32)),
    sqlalchemy.Column("email", sqlalchemy.String(128)),
    sqlalchemy.Column("password", sqlalchemy.String(128)),
)

class UserIn(BaseModel):
    name: str = Field(min_length=2, max_length=40)
    surname: str = Field(min_length=2, max_length=40)
    email: str = Field(min_length=6, max_length=40)
    password: str


class User(UserIn):
    id: int

goods = sqlalchemy.Table(
    "goods", metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String(32)),
    sqlalchemy.Column("description", sqlalchemy.String(128)),
    sqlalchemy.Column("price", sqlalchemy.Integer),
)


class Goods(BaseModel):
    name: str = Field(min_length=2, max_length=40)
    description: str = Field(max_length=100)
    price: float


class GoodsIn(Goods):
    id: int

orders = sqlalchemy.Table(
    "orders", metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("customer_id", sqlalchemy.ForeignKey("users.id")),
    sqlalchemy.Column("item_id", sqlalchemy.ForeignKey("goods.id")),
    sqlalchemy.Column("order_date", DateTime, default=datetime.now(), nullable=False),
    sqlalchemy.Column("status", sqlalchemy.Boolean),
)

class Order(BaseModel):
    customer_id: int
    item_id: int
    order_date: datetime = Field(...)
    status: bool


class OrderIn(Order):
    id: int


engine = sqlalchemy.create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
metadata.create_all(engine)