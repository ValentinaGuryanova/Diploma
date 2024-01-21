from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_async_session
from src.products.models import product
from src.products.schemas import ProductCreate

router = APIRouter(
    prefix="/products",
    tags=["Product"]
)


@router.get("/")
async def get_products(product_is_active: bool, session: AsyncSession = Depends(get_async_session)):
    try:
        query = select(product).where(product.c.is_active == product_is_active)
        result = await session.execute(query)
        return {
            "status": "success",
            "data": result.all(),
            "details": None
        }
    except Exception:
        raise HTTPException(status_code=500, detail={
            "status": "error",
            "data": None,
            "details": None
        })


@router.post("/")
async def add_products(new_product: ProductCreate, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(product).values(**new_product.dict())
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}


@router.get("/")
async def get_all_products(limit: int = 1, offset: int = 0):
    return ProductCreate[offset:][:limit]


@router.put("/update/{product_id}")
async def update_product(product_id: int, new_name: str, new_price: int):
    current_product = list(filter(lambda product: product.get("id") == product_id, ProductCreate))[0]
    current_product["name"] = new_name
    current_product["price"] = new_price
    return {"status": 200, "data": current_product}


@router.delete("/delete/{product_id}")
async def delete_product(product_id: int):
    pass
