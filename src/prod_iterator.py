from typing import Any

from src.category import Category, Product


class ProductIterator:

    def __init__(self, category):
        self.category = category
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self) -> Any:
        if self.index < len(self.category.product_list):
            product = self.category.product_list[self.index]
            self.index += 1
            return product
        else:
            raise StopIteration


