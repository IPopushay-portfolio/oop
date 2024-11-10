from src.category import Category


def test_category_init_(product, category) -> None:
    assert product.name == "Samsung Galaxy S23 Ultra"
    assert product.description == "256GB, Серый цвет, 200MP камера"

    assert category.name == "Смартфоны"
    assert category.description == (
        "Смартфоны, как средство не только "
        "коммуникации, но и получения "
        "дополнительных функций для удобства"
        " жизни"
    )
    assert Category.product_count == 2
    assert Category.category_count == 1


def test_product_init_(category, prod_3) -> None:
    category.add_product(prod_3)
    assert category.name == "Смартфоны"
    assert category.description == (
        "Смартфоны, как средство не только "
        "коммуникации, но и получения "
        "дополнительных функций для удобства"
        " жизни"
    )
    assert Category.product_count == 3
    assert Category.category_count == 1
    assert category.products == (
        "Samsung Galaxy S23 Ultra, 180000.0 руб. " "Остаток 5 шт.\nIphone 15, 210000.0 руб. " "Остаток 8 шт.\n"
    )
