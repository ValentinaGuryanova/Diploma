from fastapi import FastAPI
from fastapi_sqlalchemy import DBSessionMiddleware

from src.database import DATABASE_URL
from src.products.router import router as router_product
from src.user.router import router as router_user
from src.user.router import router as router_token

app = FastAPI(
    title="Cosmetics Shop"
)

app.add_middleware(
            DBSessionMiddleware,
            db_url=DATABASE_URL,
        )

app.include_router(router_product)
app.include_router(router_user)
app.include_router(router_token)


@app.on_event("startup")
async def startup():
    from src.database import Base, engine
    from src.products.models import Product  # noqa
    from src.user.models import User, Token   # noqa
    Base.metadata.create_all(bind=engine)
