from pydantic import BaseModel, EmailStr


class Token(BaseModel):

    access_token: str
    #token_type: str


class TokenData(BaseModel):
    username: str | None = None


class User(BaseModel):

    username: str
    email: EmailStr
    phone_number: str
    password: str


class UserInDB(User):
    hashed_password: str
