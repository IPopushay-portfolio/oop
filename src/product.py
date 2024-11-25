from abc import ABC, abstractmethod

from src.print_mixin import PrintMixin


class BaseProduct(ABC):
    @abstractmethod
    def __add__(self, other):
        pass


class Product(BaseProduct, PrintMixin):
    """Создан класс Product"""

    name: str
    description: str
    price: float
    quantity: int
    product_list: list
    pay: float
    """Для класса Product определены свойства"""

    def __init__(self, name: str, description: str, price: float, quantity: int, product_list=None):
        """Функция опеределяет конструктор класса Product и его атрибуты
        (свойства)"""
        self.name = name
        self.description = description
        self.__price = price
        if quantity != 0:
            self.quantity = quantity
        else:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")
        self.__product_list = product_list
        self.pay = self.price * self.quantity
        super().__init__()

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value: int):
        if value <= 0:
            print("Цена не должна быть 0 или < 0")
        else:
            self.__price = value

    def __str__(self):
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        return (self.__price * self.quantity) + (other.__price * other.quantity)

    @classmethod
    def new_product(cls, dict_product):
        name = dict_product.get("name")
        description = dict_product.get("description")
        price = dict_product.get("price")
        quantity = dict_product.get("quantity")
        return cls(name, description, price, quantity)

    def __repr__(self):
        return (
            f"Product(name = {self.name}, description = "
            f"{self.description}, price = {self.price}, "
            f"quantity = {self.quantity})"
        )


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
