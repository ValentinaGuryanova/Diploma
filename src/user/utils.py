from fastapi import HTTPException, FastAPI
from fastapi_sqlalchemy import db
from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase
from sqlalchemy.orm import Session
from starlette.requests import Request
from passlib.context import CryptContext
from src.user.models import User, Token

app = FastAPI(
    title="Product Shop"
)

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


async def get_user_db():
    yield SQLAlchemyUserDatabase(db.session, User)


async def register(db: Session, user_data: User):
    if User.email == user_data:
        raise HTTPException(status_code=400, detail="Пользователь с таким email уже существует!")
    user = User(email=user_data.email)
    user.hashed_password = pwd_context.hash(user_data.password)
    db.add(user)
    db.commit()
    return {"email": user.email}


async def auth(request: Request):
    user = SQLAlchemyUserDatabase(db.session, User)
    token = request.headers.get("token")
    if not token:
        raise HTTPException(status_code=403, detail="Токен не передан")
    user = user.get_by_email(db.session(Token).filter(token=token).one())
    print(user)
    if user:
        yield user
    else:
        raise HTTPException(status_code=403, detail="Пользователь не авторизован")
