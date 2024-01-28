from fastapi import APIRouter, Depends, HTTPException
from fastapi_sqlalchemy import db
from sqlalchemy.orm import Session

from src.user.models import User
from src.user.utils import pwd_context, get_user_db, create_user
from src.user import schemas
from src.user.schemas import User, UserInDB

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
async def register(db: Session, user: User):
    db.session.query(User).all()
    if user.email in db:
        raise HTTPException(status_code=400, detail="Пользователь с таким email уже существует!")
    create_user(user)
    return {"message": "Пользователь успешно зарегистрирован."}

