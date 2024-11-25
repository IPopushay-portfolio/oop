from typing import Any

import pytest
from pyexpat.errors import messages

from src.category import Category
from src.product import Product


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
def category(product1: Product, product2: Product, product3: Product) -> Any:
    return Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, " "но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3],
    )


@pytest.fixture
def test_product_init_(product_samsung):
    assert product_samsung.name == "Samsung Galaxy S23 Ultra"
    assert product_samsung.description == "256GB, Серый цвет, 200MP камера"


@pytest.fixture
def test_category_init_(category_smartphone):
    assert category_smartphone.name == "Смартфоны"
    assert category_smartphone.description == (
        "Смартфоны, как средство не только коммуникации, но и получения" "дополнительных функций для удобства жизни"
    )
    assert category_smartphone.category_count == 1
    assert category_smartphone.product_count == 3


@pytest.fixture
def test_adding_product(product_samsung, product_iphone):
    prod_sum = product_samsung + product_iphone
    assert prod_sum == 2580000.0


@pytest.fixture
def test_str_product(product_samsung):
    prod_str = str(product_samsung)
    assert prod_str == "Samsung Galaxy S23 Ultra"


@pytest.fixture
def test__add__product(product_grass, product_smartphone):
    with pytest.raises(TypeError):
        assert product_grass + product_smartphone == TypeError


@pytest.fixture
def test_prod_iterator(prod_iterator):
    iter(prod_iterator)
    assert prod_iterator.index == 0
    assert next(prod_iterator).name == "Samsung Galaxy S23 Ultra"


@pytest.fixture
def test_category_add_product(capsys, product) -> None:
    product.name = "Samsung Galaxy S23 Ultra"
    message = capsys.readouterr()
    assert message.out.strip().split("\n")[-1] == "Samsung Galaxy S23 Ultra"

    successfully = messages[0] if len(messages) > 0 else ""
    assert successfully == "Товар 'Samsung Galaxy S23 Ultra' успешно добавлен"

    completed = messages[1] if len(messages) > 1 else ""
    assert completed == "Обработка завершена успешно"


def test_print_mixin(capsys):

    Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    message = capsys.readouterr()
    assert message.out.strip() == Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    assert message.out.strip() == Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    assert message.out.strip() == Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)


def test_custom_exception(capsys, message):
    assert len(message) == 1
