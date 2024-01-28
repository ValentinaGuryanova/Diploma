from fastapi import APIRouter, HTTPException
from fastapi_sqlalchemy import db
from src.user.schemas import UserCreate, UserIn, User, UserOut
from src.user.utils import create_user, create_access_token

router = APIRouter(
    prefix="/users",
    tags=["User"]
)


@router.get("/")
async def get_user():
    data = db.session.query(UserCreate).all()
    return {
        "status": "success",
        "data": data,
        "details": None
    }


@router.post("/user/")
async def register(user: UserCreate):
    db.session.query(User).all()
    if user.email in db:
        raise HTTPException(status_code=400, detail="Пользователь с таким email уже существует!")
    create_user(user)
    return {"message": "Пользователь успешно зарегистрирован!"}


@router.post("/login/")
async def login(user: UserIn):
    db.session.query(User).all()
    if user.email in db:
        stored_user = db[user.email]
        if user.password == stored_user["password"]:
            return UserOut(username=stored_user["username"], email=stored_user.get("email"))
    raise HTTPException(status_code=401, detail="Неправильный email или password")