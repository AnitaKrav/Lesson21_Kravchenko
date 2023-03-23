from typing import Dict

from classes.BaseStorage import BaseStorage
from exceptions import DifferentProduct


class Shop(BaseStorage):

    def __init__(self, items: Dict[str, int], capacity: int=20):
        self.__items = items
        self.__capacity = capacity
        super().__init__(items, capacity)

    def add(self, name: str, amount: int):
        if name not in self.__items and self.get_unique_items_count() == 5:
            raise DifferentProduct
        super().add(name, amount)
