from typing import Dict

from classes.BaseStorage import BaseStorage


class Store(BaseStorage):

    def __init__(self, items: Dict[str, int], capacity: int=100):
        self.__items = items
        self.__capacity = capacity
        super().__init__(items, capacity)
