from fastapi import APIRouter, Depends

from src.auth.models import User

router = APIRouter(
    prefix="/users",
    tags=["User"]
)


@router.get("/{user_id}")
async def get_user(user_id: int):
    return [user for user in User if user.get("id") == user_id]


@router.post("/{user_id}")
async def change_username(user_id: int, new_name: str):
    current_user = list(filter(lambda user: user.get("id") == user_id, User))[0]
    current_user["username"] = new_name
    return {"status": 200, "data": current_user}
