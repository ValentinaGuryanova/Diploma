import re
from typing import Optional

from pydantic import BaseModel, EmailStr, constr
from pydantic.v1 import validator


class UserBase(BaseModel):

    username: str
    email: EmailStr
    #phone_number: constr(regex=r'^\+7\d{10}$')
    phone_number: constr(min_length=12, max_length=12)

    @validator('phone_number')
    def phone_number_must_be_valid(cls, v):
        if re.match(r'^\+7\d{10}$', v) is None:
            raise ValueError("Неверно указан формат номера телефона")
        return v


class UserIn(BaseModel):
    email: EmailStr
    password: constr(min_length=8)

    @validator('password')
    def phone_number_must_be_valid(cls, v):
        if re.match(r'^(?=.*[A-Z])(?=.*[$%&!:.]).*$', v) is None:
            raise ValueError("Пароль должен иметь не менее 8 символов, как минимум одна заглавная, строчная буква и цифра")
        return v


class UserOut(BaseModel):
    username: str
    email: Optional[str] = None


class UserCreate(UserBase):
    password: str
    #access_token: str = None


class UserAll(UserBase):
    id: int
    is_active: bool = True
    is_superuser: bool = False
    is_verified: bool = False
    access_token: str = None


class UserInDB(UserAll):
    hashed_password: str


class Token(BaseModel):
    access_token: str


class TokenData(BaseModel):
    username: str | None = None