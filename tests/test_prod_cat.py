def test_product_init_(product_samsung):
    assert product_samsung.name == "Samsung Galaxy S23 Ultra"
    assert product_samsung.description == "256GB, Серый цвет, 200MP камера"


def test_category_init_(category_smartphone):
    assert category_smartphone.name == "Смартфоны"
    assert category_smartphone.description == (
        "Смартфоны, как средство не только коммуникации, но и получения " "дополнительных функций для удобства жизни"
    )
    assert category_smartphone.category_count == 1
    assert category_smartphone.product_count == 3


def test_prod_iterator(prod_iterator):
    iter(prod_iterator)
    assert prod_iterator.index == 0
    assert next(prod_iterator).name == "Samsung Galaxy S23 Ultra"
