from datetime import datetime

from sqlalchemy import Column, Integer, String, TIMESTAMP, Boolean

from src.database import Base


class Product(Base):
    """ Модель товаров """

    __tablename__ = "product"
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    price = Column(Integer, nullable=False)
    create_at = Column(TIMESTAMP, default=datetime.utcnow)
    update_at = Column(TIMESTAMP, default=datetime.utcnow)
    is_active = Column(Boolean, default=True)




