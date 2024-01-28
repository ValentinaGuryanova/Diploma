from typing import Annotated

from fastapi import HTTPException, FastAPI, Depends
from fastapi_sqlalchemy import db
from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase
from sqlalchemy import select
from sqlalchemy.orm import Session
from starlette.requests import Request
from passlib.context import CryptContext
from src.user.models import User
from src.user import schemas
from src.user.schemas import UserInDB, Token
from fastapi.security import OAuth2PasswordBearer

app = FastAPI(
    title="Product Shop"
)

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


async def get_user_db():
    yield SQLAlchemyUserDatabase(db.session, UserInDB)


async def get_password_hash(password):
    return pwd_context.hash(password)


async def create_user(db: Session, user: User):
    pwd_context.hash(user.password)
    db.add(user)
    db.commit()
    return user


async def auth(request: Request):
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


def fake_decode_token(token):
    return User(
        username=token + "fakedecoded", email="john@example.com", full_name="John Doe"
    )


async def get_current_user(token: Annotated[str, Depends()]):
    user = fake_decode_token(token)
    return user
