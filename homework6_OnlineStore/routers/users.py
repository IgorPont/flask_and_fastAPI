from fastapi import APIRouter, Query, HTTPException
from homework6_OnlineStore.models.user_models import UserIn, User, UserUpdate
from homework6_OnlineStore.database import users, db
# хеширование паролей
from bcrypt import gensalt, hashpw

router = APIRouter()


@router.get("/users", response_model=list[User], response_model_exclude={"password"})
async def get_users(
        skip: int = Query(default=None, title="Skip count", ge=0),
        count: int = Query(default=None, title="Get count", ge=0),
):
    query = users.select().offset(skip).limit(count)
    return await db.fetch_all(query=query)


@router.get("/users/{user_id}", response_model=User)
async def get_user_by_id(user_id: int):
    query = users.select().where(users.c.id == user_id)
    data = await db.fetch_one(query=query)
    if not data:
        raise HTTPException(status_code=404, detail="User not found")
    return data


@router.post("/users", response_model=User)
async def create_user(user: UserIn):
    salt = gensalt()
    password_hash = hashpw(user.password.encode("utf-8"), salt=salt)
    user.password = password_hash.decode("utf-8")
    query = users.insert().values(**user.model_dump())
    user_id = await db.execute(query=query)
    return User(**user.model_dump(), id=user_id)


@router.put("/users/{user_id}", response_model=User)
async def update_user(user_id: int, user: UserUpdate):
    query = users.update().where(users.c.id == user_id).values(**user.model_dump())
    res = await db.execute(query=query)
    if res > 0:
        return User(**user.model_dump(), id=user_id)
    raise HTTPException(status_code=404, detail="User not found")


@router.delete("/users/{user_id}", response_model=dict)
async def delete_user(user_id: int):
    query = users.delete().where(users.c.id == user_id)
    res = await db.execute(query=query)
    if res > 0:
        return {"message": "User was successfully deleted"}
    raise HTTPException(status_code=404, detail="User not found")
