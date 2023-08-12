from databases import Database
from sqlalchemy import MetaData, Column, Integer, String, Table, create_engine, Float, Date, ForeignKey
from sqlalchemy.orm import relationship

from settings import settings
from datetime import datetime

db = Database(settings.DATABASE_URL)
metadata = MetaData()

engine = create_engine(settings.DATABASE_URL, connect_args={"check_same_thread": False})

users = Table(
    "users",
    metadata,
    Column('id', Integer, primary_key=True),
    Column('firstname', String(settings.NAME_MAX_LENGTH)),
    Column('lastname', String(settings.NAME_MAX_LENGTH)),
    Column('email', String(settings.EMAIL_MAX_LENGTH)),
    Column('password', String(settings.PASSWORD_MAX_LENGTH)),

)

products = Table(
    "products",
    metadata,
    Column('id', Integer, primary_key=True),
    Column('title', String(settings.STRING_MAX_LENGTH)),
    Column('description', String(settings.STRING_MAX_LENGTH)),
    Column('price', Float()),

)

orders = Table(
    "orders",
    metadata,
    Column('id', Integer, primary_key=True),
    Column('user_id', Integer, ForeignKey('users.id')),
    Column('product_id', Integer, ForeignKey('products.id')),
    Column('order_date', Date(), default=datetime.now()),
    Column('order_status', String(settings.STRING_MAX_LENGTH)),

)

metadata.create_all(engine)
