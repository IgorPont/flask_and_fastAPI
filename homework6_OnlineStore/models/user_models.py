from pydantic import BaseModel, Field, EmailStr
from homework6_OnlineStore.settings import settings


class UserIn(BaseModel):
    firstname: str = Field(..., min_length=settings.NAME_MIN_LENGTH, max_length=settings.NAME_MAX_LENGTH)
    lastname: str = Field(..., min_length=settings.NAME_MIN_LENGTH, max_length=settings.NAME_MAX_LENGTH)
    email: EmailStr = Field(..., min_length=settings.EMAIL_MIN_LENGTH, max_length=settings.EMAIL_MAX_LENGTH)
    password: str = Field(..., min_length=settings.PASSWORD_MIN_LENGTH)


class UserUpdate(BaseModel):
    firstname: str = Field(..., min_length=settings.NAME_MIN_LENGTH, max_length=settings.NAME_MAX_LENGTH)
    lastname: str = Field(..., min_length=settings.NAME_MIN_LENGTH, max_length=settings.NAME_MAX_LENGTH)
    email: EmailStr = Field(..., min_length=settings.EMAIL_MIN_LENGTH, max_length=settings.EMAIL_MAX_LENGTH)


class User(UserUpdate):
    id: int
