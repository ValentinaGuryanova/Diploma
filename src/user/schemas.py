from typing import Optional

from pydantic import BaseModel, EmailStr, constr, model_validator


class UserBase(BaseModel):

    username: str
    email: EmailStr
    phone_number: constr(pattern=r'^\+7\d{10}$')


class UserIn(BaseModel):
    email: EmailStr
    password: constr(min_length=8)

    @model_validator(mode='before')
    @classmethod
    def password_validation(cls, v):
        if not any(char.isupper() for char in v['password']):
            raise ValueError('Пароль должен содержать заглавную букву!')
        if not any(char in '$%&!:.' for char in v['password']):
            raise ValueError('Пароль должен содержать один из специальных символов: $%&!:.')
        return v


class UserOut(BaseModel):
    username: str
    email: Optional[str] = None


class UserCreate(UserBase):
    password: str

    @model_validator(mode='before')
    @classmethod
    def password_validation(cls, v):
        if not any(char.isupper() for char in v['password']):
            raise ValueError('Пароль должен содержать заглавную букву!')
        if not any(char in '$%&!:.' for char in v['password']):
            raise ValueError('Пароль должен содержать один из специальных символов: $%&!:.')
        return v


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