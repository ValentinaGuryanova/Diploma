from fastapi import APIRouter, HTTPException
from fastapi_sqlalchemy import db
from src.user.schemas import UserCreate
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
    db.session.query(UserCreate).all()
    if user.email in db:
        raise HTTPException(status_code=400, detail="Пользователь с таким email уже существует!")
    create_user(user)
    token = create_access_token(user)
    return {
        "message": "Пользователь успешно зарегистрирован.",
        "access_token": token
        }
