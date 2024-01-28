from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


async def test_add_products():
    response = await client.post("/products", json={
        "id": 1,
        "name": "lipstick",
        "price": 500,
        "created_at": "2024-01-21T00:00:00",
        "updated_at": "2024-01-21T00:00:00",
        "is_active": True
    })

    assert response.status_code == 200


async def test_get_products():
    response = await client.post("/products", json={
        "id": 1,
        "name": "lipstick",
        "price": 500,
        "created_at": "2024-01-21T00:00:00",
        "updated_at": "2024-01-21T00:00:00",
        "is_active": True
    })
    product_id = response.json()["id"]
    response = await client.get(f"/products/{product_id}")

    assert response.status_code == 200
    assert response.json()["status"] == "success"
    assert len(response.json()["data"]) == 1


async def test_update_product():
    response = await client.post("/products", json={
        "id": 1,
        "name": "lipstick",
        "price": 500,
        "created_at": "2024-01-21T00:00:00",
        "updated_at": "2024-01-21T00:00:00",
        "is_active": True
    })
    product_id = response.json()["id"]
    response = await client.put(f"/products/{product_id}", json={
        "id": 1,
        "name": "lipsticks",
        "price": 800,
        "created_at": "2024-01-21T00:00:00",
        "updated_at": "2024-01-21T00:00:00",
        "is_active": True
    })
    assert response.status_code == 200
    assert response.json()["name"] == "new_name"
    assert response.json()["price"] == "new_price"


async def test_delete_product():
    response = await client.post("/products", json={
        "id": 1,
        "name": "lipstick",
        "price": 500,
        "created_at": "2024-01-21T00:00:00",
        "updated_at": "2024-01-21T00:00:00",
        "is_active": True
    })
    product_id = response.json()["id"]
    response = client.delete(f"/products/{product_id}")

    assert response.status_code == 200
    assert response.json()["status"] == "success"
