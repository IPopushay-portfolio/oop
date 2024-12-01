from src.product import Product


class LawnGrass(Product):
    """Создан класс Lawngrass"""

    country: str
    germination_period: str
    color: str

    def __init__(
        self,
        name: str,
        description: str,
        __price: float,
        quantity: int,
        country: str,
        germination_period: str,
        color: str,
        __product_list=None,
    ):
        super().__init__(name, description, __price, quantity, __product_list)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __add__(self, other):
        if type(other) is LawnGrass:
            return (self.price * self.quantity) + (other.price * other.quantity)
        raise TypeError


