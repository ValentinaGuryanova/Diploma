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
    data = db.session.query(Product).all()
    return {
            "status": "success",
            "data": data,
            "details": None
        }


@router.post("/")
async def add_products(new_product: ProductCreate, _=Depends(auth)):
    db.session.add(Product(**new_product.model_dump()))
    return {"status": "success"}


@router.put("/update/{product_id}")
async def update_product(product_id: int, new_name: str, new_price: int, _=Depends(auth)):
    current_product = list(filter(lambda product: product.get("id") == product_id, ProductCreate))[0]
    current_product["name"] = new_name
    current_product["price"] = new_price
    return {"status": 200, "data": current_product}


@router.delete("/delete/{product_id}")
async def delete_product(product_id: int, _=Depends(auth)):
    db.session.query(Product).delete(product_id)
    return {"status": "success"}
