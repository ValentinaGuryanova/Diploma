from pydantic import BaseModel, EmailStr


class Token(BaseModel):
    access_token: str


class TokenData(BaseModel):
    username: str | None = None


class UserBase(BaseModel):

    username: str
    email: EmailStr
    phone_number: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool = True
    is_superuser: bool = False
    is_verified: bool = False
    access_token: str = None


class UserInDB(User):
    hashed_password: str
