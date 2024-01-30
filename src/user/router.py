from fastapi import APIRouter, HTTPException
from fastapi_sqlalchemy import db
from sqlalchemy.exc import IntegrityError

from src.user.utils import create_user, auth
from src.user.models import User
from src.user.schemas import UserCreate, UserIn

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
    try:
        create_user(User(**user.model_dump()))
        return {"message": "Пользователь успешно зарегистрирован."}
    except IntegrityError as e:
        raise HTTPException(status_code=400, detail="Пользователь с таким email уже существует!")
    except Exception as e:
        raise HTTPException(status_code=404, detail="Что-то пошло не так!")


@router.post("/login/")
async def login(user: UserIn):
    try:
        auth(User(**user.model_dump()))
        return {"message": "Вы авторизованы!"}
    except IntegrityError as e:
        raise HTTPException(status_code=400, detail="Пользователь с таким email уже авторизован!")
    except Exception as e:
        raise HTTPException(status_code=404, detail="Неправильный email или password")
