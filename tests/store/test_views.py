import pytest
from rest_framework.test import APIClient

from tests.factories.store import ProductFactory


@pytest.mark.django_db
def test_get_product_list():
    ProductFactory.create_batch(3)

    client = APIClient()

    response = client.get("/api/products/")

    assert response.status_code == 200
    assert len(response.data) == 3


@pytest.mark.django_db
def test_get_single_product():
    product = ProductFactory()

    client = APIClient()

    response = client.get(f"/api/products/{product.id}/")

    assert response.status_code == 200
    assert response.data["name"] == product.name
    assert response.data["quantity"] == product.quantity


@pytest.mark.django_db
def test_reduce_stock_success():
    product = ProductFactory(quantity=10)

    client = APIClient()

    url = f"/api/products/{product.id}/reduce_stock/5/"
    response = client.post(url)

    product.refresh_from_db()
    assert response.status_code == 200
    assert product.quantity == 5


@pytest.mark.django_db
def test_reduce_stock_insufficient_quantity():
    product = ProductFactory(quantity=3)

    client = APIClient()

    url = f"/api/products/{product.id}/reduce_stock/5/"
    response = client.post(url)

    assert response.status_code == 400


@pytest.mark.django_db
def test_reduce_stock_invalid_amount():
    product = ProductFactory(quantity=10)

    client = APIClient()

    url = f"/api/products/{product.id}/reduce_stock/-5/"
    response = client.post(url)

    assert response.status_code == 404
