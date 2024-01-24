from fastapi import APIRouter, Depends
from fastapi_sqlalchemy import db
from sqlalchemy.orm import Session

from src.user.models import User
from src.user.utils import register
from src.user import schemas

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
def register_user(user_data: schemas.User, db: Session = Depends()):
    return register(db=db, user_data=user_data)
