import re
import uvicorn
import asyncpg
from fastapi import FastAPI, Depends, HTTPException, Query
from fastapi_users import FastAPIUsers

from src.auth.base_config import auth_backend
from src.auth.models import User
from src.auth.manager import get_user_manager
from src.auth.schemas import UserRead, UserCreate
from src.config import DB_USER, DB_PASS, DB_NAME, DB_HOST

from src.products.router import router as router_product
from src.auth.router import router as router_user

app = FastAPI(
    title="Product Shop"
)

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)

app.include_router(router_product)

app.include_router(router_user)

current_user = fastapi_users.current_user()


@app.get("/protected-route")
def protected_route(user: User = Depends(current_user)):
    return f"Hello, {user.username}"


@app.get("/unprotected-route")
def unprotected_route():
    return f"Hello, anonym"


@app.get("/check_phone/")
async def check_phone(phone_number: str = Query(length=12)):
    if phone_number[:2] == "+7" and len(phone_number) == 12:
        return {phone_number}
    else:
        raise HTTPException(status_code=400,
                            detail=f"Телефон {phone_number} не соответствует заданному формату")


@app.get("/check_password/")
async def check_password(password: str = Query(min_length=8), password2: str= Query(min_length=8)):
    if re.search(r"[a-z]", password) and re.search(r"[A-Z]", password) and re.search(r"[0-9]", password) and re.search(r"[$%&!:.]", password):
        if password2 == password:
            return {"message": "Пароль создан успешно!"}
    else:
        raise HTTPException(status_code=400,
                            detail=f"Пароль не соответствует заданному формату")


@app.on_event("startup")
async def startup():
    app.state.db = await asyncpg.connect(
        user=DB_USER,
        password=DB_PASS,
        database=DB_NAME,
        host=DB_HOST
    )


@app.on_event("shutdown")
async def shutdown():
    await app.state.db.close()
