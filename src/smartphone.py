from src.product import Product


class Smartphone(Product):
    """Создан класс Smartphone"""

    efficiency: float
    model: str
    memory: float
    color: str

    def __init__(
        self,
        name: str,
        description: str,
        __price: float,
        quantity: int,
        efficiency: float,
        model: str,
        memory: float,
        color: str,
        __product_list=None,
    ):
        """Функция опеределяет конструктор класса Product и его атрибуты
        (свойства)"""
        super().__init__(name, description, __price, quantity, __product_list)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __add__(self, other):
        if type(other) is Smartphone:
            return (self.price * self.quantity) + (other.price * other.quantity)
        raise TypeError


