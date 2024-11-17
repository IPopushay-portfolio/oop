class Product:
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
        self.quantity = quantity
        self.__product_list = product_list
        self.pay = self.price * self.quantity

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
        if type(other) is Product:
            return (self.__price * self.quantity) + (other.__price * other.quantity)
        raise TypeError

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
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    print(str(product1))
    print(str(product2))
    print(str(product3))
