from src.product import Product


class Category:
    """Создан класс Category"""

    name: str
    description: str
    products: int
    product_list: list
    category_count = 0
    product_count = 0
    """Для класса Category определены свойства"""

    def __init__(self, name: str, description: str, products: int, product_list=None):
        """Функция опеределяет конструктор класса Category и его атрибуты
        (свойства)"""
        self.name = name
        self.description = description
        self.__products = products if products else []
        self.__products.append(products)
        self.product_list = product_list
        Category.category_count += 1

    def __str__(self):
        return f"{self.name}, количество продуктов: {self.product_list} шт."

    @property
    def products(self):
        new_str = ""
        for product in self.__products:
            new_str += f"{str(product)}\n"
            return new_str

    def add_product(self, product: Product):
        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1
        raise TypeError


if __name__ == "__main__":
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    print(str(product1))
    print(str(product2))
    print(str(product3))

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3],
    )

    print(str(category1))

    print(category1.products)

    print(product1 + product2)
    print(product1 + product3)
    print(product2 + product3)
