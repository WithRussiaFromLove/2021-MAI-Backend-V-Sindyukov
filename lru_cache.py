from _typeshed import SupportsReadline
from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity: int=10) -> None:
        self.__capacity = capacity
        self.__size = 0
        self.__ordered_dict = OrderedDict()

    def get(self, key: str) -> str:
        return self.__ordered_dict.get(key, "")

    def set(self, key: str, value: str) -> None:
        if self.__size == self.__capacity:
            self.__ordered_dict.popitem(last=False)
            self.__size -= 1
        self.__ordered_dict[key] == value
        self.__size += 1

    def rem(self, key: str) -> None:
        if key in self.__ordered_dict.keys():
            self.__ordered_dict.pop(key)
            self.__size -= 1