from typing import AsyncGenerator

from fastapi_sqlalchemy import db
from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase
from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base
from sqlalchemy.orm import sessionmaker

from src.config import DB_USER, DB_PASS, DB_HOST, DB_PORT, DB_NAME
from src.user.schemas import UserAll

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
Base: DeclarativeMeta = declarative_base()


engine = create_engine(DATABASE_URL)
#async_session_maker = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async_session = sessionmaker(
        engine,
        class_=AsyncSession,  # type: ignore
        expire_on_commit=False,
        )
    async with async_session() as session:
        yield session
        await session.close()


def get_user_db():
     yield SQLAlchemyUserDatabase(db.session, UserAll)
