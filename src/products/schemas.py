from datetime import datetime

from pydantic import BaseModel


class Product(BaseModel):
    """ Модель товара """

    id: int
    name: str
    price: int
    create_at: datetime
    update_at: datetime
    is_active: bool


class ProductCreate(BaseModel):
    """ Модель товара """

    name: str
    price: int
    create_at: datetime
    update_at: datetime
    is_active: bool
