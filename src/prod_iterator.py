from src.category import Category, Product


class ProductIterator:

    def __init__(self, category):
        self.category = category
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.category.product_list):
            product = self.category.product_list[self.index]
            self.index += 1
            return product
        else:
            raise StopIteration


if __name__ == "__main__":
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    print(product1.name)
    print(product1.description)
    print(product1.price)
    print(product1.quantity)

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения " "дополнительных функций для удобства жизни",
        [product1, product2, product3],
    )

    iterator = ProductIterator(category1)
    for i in iterator:
        print(i)