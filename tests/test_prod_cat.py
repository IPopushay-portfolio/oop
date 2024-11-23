import pytest


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
