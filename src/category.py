from abc import ABC, abstractmethod

from src.exceptions import ValueError
from src.product import Product

# from itertools import product


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
        return (
            f"{self.__class__.__name__}({self.product.name}, куплено {self.buy_count} шт."
            f"Итоговая стоимость {self.total_price})"
        )


class Category(ABC):
    """Создан класс Category"""

    name: str
    description: str
    products: list
    product_list: list
    category_count = 0
    product_count = 0
    """Для класса Category определены свойства"""

    def __init__(self, name: str, description: str, products: list, product_list=None):
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

    def middle_price(self):
        try:
            return sum([product.price for product in self.product_list]) / len(self.product_list)
        except ZeroDivisionError:
            return 0

    def add_product(self, __products):
        if isinstance(__products, Category):
            try:
                if Category.products == 0:
                    raise ValueError("В категории нет товара")
            except ValueError as e:
                print(str(e))
            else:
                self.__products.append(__products)
                Category.category_count += 1
                print("Задача выполнена успешно")
            finally:
                print("Обработка добавления задачи завершена")
        else:

            raise TypeError
        return self.category_count + self.category_count


if __name__ == "__main__":
    try:
        product_invalid = Product("Бракованный товар", "Неверное количество", 1000.0, 0)
    except ValueError as e:
        print(
            "Возникла ошибка ValueError прерывающая работу программы при попытке добавить продукт с "
            "нулевым количеством"
        )
    else:
        print("Не возникла ошибка ValueError при попытке добавить продукт с нулевым количеством")

    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    category1 = Category("Смартфоны", "Категория смартфонов", [product1, product2, product3])

    print(category1.middle_price())

    category_empty = Category("Пустая категория", "Категория без продуктов", [])
    print(category_empty.middle_price())
