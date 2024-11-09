from product import Product


class Category:
    """Создан класс Category"""

    name: str
    description: str
    products: int
    product_list: list
    category_count = 0
    all_cat_count = 0
    product_count = 0
    all_prod_count = 0
    """Для класса Category определены свойства"""

    def __init__(self, name, description, products, product_list=None):
        """Функция опеределяет конструктор класса Category и его атрибуты
        (свойства)"""
        self.name = name
        self.description = description
        self.products = products
        self.product_list = product_list if product_list else []
        Category.category_count += 1
        Category.all_cat_count += len(product_list) if product_list else 0


if __name__ == "__main__":
    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, "
        "но и получения дополнительных "
        "функций для удобства жизни",
        [Product],
    )

    print(category1.name == "Смартфоны")
    print(category1.description)
    print(len(category1.product_list))
    print(category1.category_count)
    print(category1.product_count)

    product4 = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
    category2 = Category("Телевизоры", "Современный телевизор, станет вашим " "другом и помощником", [product4])

    print(category2.name)
    print(category2.description)
    print(len(category2.product_list))
    print(category2.products)

    print(Category.category_count)
    print(Category.product_count)
