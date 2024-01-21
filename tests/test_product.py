from httpx import AsyncClient


async def test_add_products(ac: AsyncClient):
    response = await ac.post("/products", json={
        "id": 1,
        "name": "lipstick",
        "price": 500,
        "created_at": "2024-01-21T00:00:00",
        "updated_at": "2024-01-21T00:00:00",
        "is_active": True
    })

    assert response.status_code == 200


async def test_get_products(ac: AsyncClient):
    response = await ac.get("/products", params={
        "product_is_active": True,
    })

    assert response.status_code == 200
    assert response.json()["status"] == "success"
    assert len(response.json()["data"]) == 1
