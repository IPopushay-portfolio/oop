from typing import Any

import pytest

from src.category import Category, Product
from src.prod_iterator import ProductIterator


@pytest.fixture
def product1() -> Any:
    return Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)


@pytest.fixture
def product2() -> Any:
    return Product("Iphone 15", "512GB, Gray space", 210000.0, 8)


@pytest.fixture
def product3() -> Any:
    return Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)


@pytest.fixture
def category(product1: Product, product2: Product) -> Any:
    return Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций " "для удобства жизни",
        [product1, product2],
    )


@pytest.fixture
def prod_iterator(prod_iterator):
    return ProductIterator(prod_iterator)


@pytest.fixture
def zero_product(some) -> Any:
    return Category(
        "Some",
        "Some",
        [some],
    )
