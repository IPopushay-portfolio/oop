class Product:
    """Создан класс Product"""

    name: str
    description: str
    price: float
    quantity: int
    product_list: list
    stock: int
    """Для класса Product определены свойства"""

    def __init__(self, name: str, description: str, price: float, quantity: int, product_list=None, stock=0):
        """Функция опеределяет конструктор класса Product и его атрибуты
        (свойства)"""
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        self.__product_list = product_list
        self.stock = stock

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
        return f"{self.name}, {self.__price} руб. {self.quantity}: шт.\n"

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
