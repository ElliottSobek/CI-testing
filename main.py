import math
from decimal import Decimal


class Main:

    @staticmethod
    def add(x: int, y: int) -> int:
        return x + y

    @staticmethod
    def double(x: int) -> int:
        return x * 2

    @staticmethod
    def root(x: int) -> Decimal:
        return Decimal(str(math.sqrt(x)))
