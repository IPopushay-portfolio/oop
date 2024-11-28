from typing import Any
import pytest
from src.category import Category
from src.product import Product
from src.smartphone import Smartphone
from src.lawngrass import LawnGrass


@pytest.fixture
def test_product1() -> Any:
    return Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)


@pytest.fixture
def test_product2() -> Any:
    return Product("Iphone 15", "512GB, Gray space", 210000.0, 8)


@pytest.fixture
def test_product3() -> Any:
    return Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0,
                   14)


@pytest.fixture
def test_product4() -> Any:
    return Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)


@pytest.fixture
def test_cat_prod1(product1: Product) -> Any:
    return Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, " "но и получения дополнительных функций для"
        " удобства жизни", [Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP "
                                                                "камера", 180000.0, 5)]
    )


def test_cat_prod2(product2: Product) -> Any:
    return Category( "Смартфоны", "Смартфоны, как средство не только коммуникации, но и получения "
                                  "дополнительных функций для удобства жизни",
                     [Product("Iphone 15", "512GB, Gray space", 210000.0, 8)])


def test_cat_prod3(product3: Product) -> Any:
    return Category(
        "Смартфоны", "Смартфоны, как средство не только коммуникации, но и получения дополнительных "
                     "функций для удобства жизни", [Product("Xiaomi Redmi Note 11",
                                                            "1024GB, Синий", 31000.0, 14)])


def test_cat2_prod4(product4: Product) -> Any:
    return Category("Телевизоры", "Современный телевизор, который позволяет наслаждаться просмотром, "
                         "станет вашим другом и помощником",
                    [Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)])


@pytest.fixture
def test_smart1_init_(smartphone1: Smartphone):
    return Smartphone("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0,
                      5, 95.5, "S23 Ultra", 256, "Серый")


def test_smart2_init_(smartphone2: Smartphone):
    return Smartphone("Iphone 15", "512GB, Gray space", 210000.0,
                      8, 98.2, "15", 512, "Gray space")


def test_smart3_init_(smartphone3: Smartphone):
    return Smartphone("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14,
                      90.3, "Note 11", 1024, "Синий")


@pytest.fixture
def test_grass1_init_(grass1: LawnGrass):
    return LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20,
                     "Россия", "7 дней", "Зеленый")


def test_grass2_init_(grass2: LawnGrass):
    return LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "США",
                     "5 дней", "Темно-зеленый")


def test_category_init(first_category, last_category):
    assert first_category.name == "Смартфоны"
    assert (first_category.description == "Смартфоны, как средство не только коммуникации, но и получения дополнительных"
                                          " функций для удобства жизни",
            first_category.product == Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера",
                                              180000.0, 5))
    assert len(first_category.products) == 3
    assert first_category.category_count == 2
    assert last_category.category_count == 2


def test_category_init2(first_category, last_category):
    assert last_category.name == "Телевизоры"
    assert (last_category.description == "Современный телевизор, который позволяет наслаждаться просмотром, станет "
                                         "вашим другом и помощником",)
    assert len(last_category.products) == 3
    assert first_category.category_count == 2
    assert last_category.category_count == 2


@pytest.fixture
def test_adding_product1(product_samsung, product_iphone):
    prod_sum = product_samsung + product_iphone
    assert prod_sum == 2580000.0


@pytest.fixture
def test_str_product1(product1):
    prod_str = str(product1)
    assert prod_str == "Samsung Galaxy S23 Ultra"


def test_str_product2(product2):
    prod_str = str(product2)
    assert prod_str == "Iphone 15", "512GB, Gray space"


def test_str_product3(product3):
    prod_str = str(product3)
    assert prod_str == "Xiaomi Redmi Note 11", "1024GB, Синий"


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
def test_category_add_product(capsys, product1) -> None:
    product1.name = "Samsung Galaxy S23 Ultra"
    message = capsys.readouterr()
    assert message.out.strip().split("\n")[-1] == "Samsung Galaxy S23 Ultra"


def test_category_add_product2(capsys, product2) -> None:
    product2.name = "Iphone 15", "512GB, Gray space"
    message = capsys.readouterr()
    assert message.out.strip().split("\n")[-1] == "Iphone 15", "512GB, Gray space"


def test_category_add_product3(capsys, product3) -> None:
    product3.name = "Xiaomi Redmi Note 11", "1024GB, Синий"
    message = capsys.readouterr()
    assert message.out.strip().split("\n")[-1] == "Xiaomi Redmi Note 11", "1024GB, Синий"


def test_print_mixin(capsys):

    Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    message = capsys.readouterr()
    assert message.out.strip() == Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    assert message.out.strip() == Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    assert message.out.strip() == Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
