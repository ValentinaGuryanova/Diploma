from fastapi import APIRouter, Depends

from fastapi_sqlalchemy import db

from src.user.utils import auth
from src.products.models import Product
from src.products.schemas import ProductCreate

router = APIRouter(
    prefix="/products",
    tags=["Product"]
)


@router.get("/")
async def get_products(_=Depends(auth)):
#async def get_products():
    data = db.session.query(Product).all()
    return {
            "status": "success",
            "data": data,
            "details": None
        }


@router.post("/")
async def add_products(new_product: ProductCreate, _=Depends(auth)):
#async def create_product(new_product: ProductCreate):
    data = db.session.add(ProductCreate(**new_product.model_dump()))
    return {
        "status": "success",
        "data": data,
        "details": None
    }


@router.put("/update/{product_id}")
#async def update_product(product_id: int, new_name: str, new_price: int):
async def update_product(product_id: int, new_name: str, new_price: int, _=Depends(auth)):
    data = db.session.query(Product).filter(lambda product: product.get("id") == product_id, ProductCreate)[0]
    data["name"] = new_name
    data["price"] = new_price
    return {"status": 200, "data": data}


@router.delete("/delete/{product_id}")
async def delete_product(product_id: int, _=Depends(auth)):
#async def delete_product(product_id: int):
    db.session.query(Product).delete(product_id)
    return {"status": "success"}
