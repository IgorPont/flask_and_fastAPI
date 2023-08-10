from pydantic import BaseModel, Field, EmailStr
from settings import settings
from datetime import date


class UserIn(BaseModel):
    firstname: str = Field(..., min_length=2, max_length=settings.NAME_MAX_LENGTH)
    lastname: str = Field(..., min_length=2, max_length=settings.NAME_MAX_LENGTH)
    birthday: date = Field(..., format="%Y.%m.%d")
    address: str = Field(..., min_length=5)
    email: EmailStr = Field(..., max_length=settings.EMAIL_MAX_LENGTH)
    password: str = Field(..., min_length=5)


class UserUpdate(BaseModel):
    firstname: str = Field(..., min_length=2, max_length=settings.NAME_MAX_LENGTH)
    lastname: str = Field(..., min_length=2, max_length=settings.NAME_MAX_LENGTH)
    birthday: date = Field(..., format="%Y.%m.%d")
    address: str = Field(..., min_length=5)
    email: EmailStr = Field(..., max_length=settings.EMAIL_MAX_LENGTH)


class User(UserUpdate):
    id: int
