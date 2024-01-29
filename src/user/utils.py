import datetime

import jwt

from fastapi import HTTPException, FastAPI, Depends
from fastapi_sqlalchemy import db
from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase
from sqlalchemy.orm import Session
from starlette.requests import Request
from passlib.context import CryptContext
from src.user.models import User

app = FastAPI(
    title="Product Shop"
)

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Секретный ключ для подписи JWT
SECRET_KEY = "v3.r.137756487.adf52d67576949fc227e9a44484f486d9ae8183c.c85c473c1a3d7451e8549432293d922bdcf27e12"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def get_password_hash(password):
    return pwd_context.hash(password)


def create_user(user: User):
    user.password = pwd_context.hash(user.password)
    db.session.add(user)
    try:
        db.session.commit()
        db.session.refresh(user)
        return user
    except Exception as e:
        db.session.rollback()
        raise HTTPException(status_code=400, detail="Ошибка при создании пользователя")


def auth(request: Request):
    user = SQLAlchemyUserDatabase(db.session, User)
    token = request.headers.get("token")
    if not token:
        raise HTTPException(status_code=403, detail="Токен не передан")
    #user = user.get_by_email(db.session(Token).filter(token=token).one())
    print(user)
    if user:
        yield user
    else:
        raise HTTPException(status_code=403, detail="Пользователь не авторизован")
