from fastapi import APIRouter, Depends, HTTPException
from fastapi_sqlalchemy import db

from src.user.utils import auth
from src.products.models import Product
from src.products.schemas import ProductCreate

router = APIRouter(
    prefix="/products",
    tags=["Product"]
)


@router.get("/")
#async def get_products(_=Depends(auth)):
async def get_products():
    try:
        data = db.session.query(Product).all()
        return data
    except Exception as e:
        raise HTTPException(status_code=404, detail="Что-то пошло не так!")


@router.post("/")
#async def add_products(new_product: ProductCreate, _=Depends(auth)):
async def add_products(new_product: ProductCreate):
    try:
        db.session.add(Product(**new_product.model_dump()))
        db.session.commit()
        return {"message": "Продукт успешно добавлен"}
    except Exception as e:
        raise HTTPException(status_code=404, detail="Что-то пошло не так!")


@router.put("/update/{product_id}")
#async def update_product(product_id: int, new_name: str = None, new_price: int = None, _=Depends(auth)):
async def update_product(product_id: int, new_name: str = None, new_price: int = None):
    try:
        data = db.session.query(Product).filter(lambda product: product.get("id") == product_id, Product)
        data["name"] = new_name
        data["price"] = new_price
        db.session.commit()
        return {"message": "Продукт успешно изменен"}
    except Exception as e:
        raise HTTPException(status_code=404, detail="Что-то пошло не так!")


@router.delete("/delete/{product_id}")
#async def delete_product(product_id: int, _=Depends(auth)):
async def delete_product(product_id: int):
    try:
        db.session.query(Product).delete(product_id)
        return {"message": "Продукт удален"}
    except Exception as e:
        raise HTTPException(status_code=404, detail="Что-то пошло не так!")