
# from jose import JWTError, jwt
# from passlib.context import CryptContext
# from datetime import datetime, timedelta

from fastapi import HTTPException, FastAPI, Depends
from fastapi_sqlalchemy import db
from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session
from starlette.requests import Request
from passlib.context import CryptContext
from src.user.models import User
from src.user import schemas
from src.user.schemas import UserInDB, Token

app = FastAPI(
    title="Product Shop"
)

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Секретный ключ для подписи JWT
SECRET_KEY = "v3.r.137756487.adf52d67576949fc227e9a44484f486d9ae8183c.c85c473c1a3d7451e8549432293d922bdcf27e12"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def get_user_db():
    yield SQLAlchemyUserDatabase(db.session, UserInDB)


def get_password_hash(password):
    return pwd_context.hash(password)


def create_user(db: Session, user: User):
    user.password = pwd_context.hash(user.password)
    db.add(user)
    try:
        db.commit()
        db.refresh(user)
        return user
    except Exception as e:
        db.rollback()
        raise e


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


# def create_access_token(data: Session, expires_delta: timedelta = None):
#     """ Функция для создания JWT-токена """
#
#     to_encode = data.copy()
#     if expires_delta:
#         expire = datetime.utcnow() + expires_delta
#     else:
#         expire = datetime.utcnow() + timedelta(minutes=15)
#     to_encode.update({"exp": expire})
#     encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
#     return encoded_jwt
