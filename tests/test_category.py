
def test_category_init_(category_count, product_count):
    assert category_count.name == "Смартфоны"
    assert category_count.description == ("Смартфоны, как средство не только "
                                          "коммуникации, но и получения "
                                          "дополнительных функций для удобства жизни"
                                          )
    assert category_count.products == "Product"
    assert len(category_count.product_list) == 2
    assert category_count.all_cat_count == 2
    assert product_count.name == "Samsung Galaxy S23 Ultra"
    assert product_count.description == "256GB, Серый цвет, 200MP камера"
    assert product_count.products == "Product"
    assert len(product_count.product_list) == 5
    assert category_count.all_cat_count == 5
