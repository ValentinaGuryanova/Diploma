from datetime import datetime

from pydantic import BaseModel


class ProductCreate(BaseModel):
    """ Модель товара """

    id: int
    name: str
    price: int
    created_at: datetime
    updated_at: datetime
    is_active: bool
