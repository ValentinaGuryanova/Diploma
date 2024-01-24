from datetime import datetime

from pydantic import BaseModel


class ProductCreate(BaseModel):
    """ Модель товара """

    name: str
    price: int
    create_at: datetime
    update_at: datetime
    is_active: bool
