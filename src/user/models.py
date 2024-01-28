from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from src.database import Base
from src.user.services import check_phone, check_password


class Token(Base):

    __tablename__ = "token"
    id = Column(Integer, primary_key=True)
    access_token = Column(String, nullable=False)
    # user_id = Column(Integer, ForeignKey("user_id"))
    # user = relationship("User", back_populates="tokens")


class User(Base):
    """ Модель пользователя """

    __tablename__ = "user"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    phone_number = Column(String, nullable=False)
    password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True, nullable=False)
    is_superuser = Column(Boolean, default=False, nullable=False)
    is_verified = Column(Boolean, default=False, nullable=False)
    access_token = relationship("Token", back_populates="user")

#    check_phone()
#    check_password()