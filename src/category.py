from abc import ABC, abstractmethod

from src.product import Product


class Abstract(ABC):
    @abstractmethod
    def __repr__(self):
        pass


class Order(Abstract):
    def __init__(self, product, buy_count):
        self.product = product
        self.buy_count = buy_count
        self.total_price = self.buy_count * product.price

    def __repr__(self):
        return f"{self.product.name}, куплено {self.buy_count} шт. Итоговая стоимость = {self.total_price}."


class Category(Abstract):
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

    print(product1.name)
    print(product1.description)
    print(product1.price)
    print(product1.quantity)

    print(product2.name)
    print(product2.description)
    print(product2.price)
    print(product2.quantity)

    print(product3.name)
    print(product3.description)
    print(product3.price)
    print(product3.quantity)

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения " "дополнительных функций для удобства жизни",
        [product1, product2, product3],
    )

    print(category1.name == "Смартфоны")
    print(category1.description)
    print(len(category1.products))
    print(category1.category_count)
    print(category1.product_count)

    product4 = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
    category2 = Category(
        "Телевизоры",
        "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим " "другом и помощником",
        [product4],
    )

    print(category2.name)
    print(category2.description)
    print(len(category2.products))
    print(category2.products)

    print(Category.category_count)
    print(Category.product_count)
