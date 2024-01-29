
from fastapi import APIRouter, HTTPException
from fastapi_sqlalchemy import db
from src.user.utils import create_user
#from src.user.models import User
from src.user.schemas import User, UserCreate

router = APIRouter(
    prefix="/users",
    tags=["User"]
)


@router.get("/")
async def get_user():
    data = db.session.query(User).all()
    return {
        "status": "success",
        "data": data,
        "details": None
    }


@router.post("/")
async def register(user: UserCreate):
    db.session.query(User).all()
    if user.email in db:
        raise HTTPException(status_code=400, detail="Пользователь с таким email уже существует!")
    create_user(user)
    return {"message": "Пользователь успешно зарегистрирован."}


@router.post("/login/")
async def login(user: User):
    db.session.query(User).all()
    if user.email in db:
        stored_user = db[user.email]
        if user.password == stored_user["password"]:
            return User(username=stored_user["username"], email=stored_user.get("email"))
    raise HTTPException(status_code=401, detail="Неправильный email или password")