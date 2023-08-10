from databases import Database
from sqlalchemy import MetaData, Column, Integer, String, Table, create_engine, Date, Text
from settings import settings

db = Database(settings.DATABASE_URL)
metadata = MetaData()

engine = create_engine(settings.DATABASE_URL, connect_args={"check_same_thread": False})

users = Table(
    "users",
    metadata,
    Column('id', Integer, primary_key=True),
    Column('firstname', String(settings.NAME_MAX_LENGTH)),
    Column('lastname', String(settings.NAME_MAX_LENGTH)),
    Column('birthday', Date()),
    Column('address', Text()),
    Column('email', String(settings.EMAIL_MAX_LENGTH)),
    Column('password', String(128)),
)

metadata.create_all(engine)
