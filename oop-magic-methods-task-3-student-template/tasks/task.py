from __future__ import annotations
from typing import Type


class Currency:
    """
    1 EUR = 2 USD = 100 GBP

    1 EUR = 2 USD    ;  1 EUR = 100 GBP
    1 USD = 0.5 EUR  ;  1 USD = 50 GBP
    1 GBP = 0.02 USD ;  1 GBP = 0.01 EUR
    """
    abr = ''
    eur, usd, pound = 1, 2, 100

    def __init__(self, value: float):
        self.value = float(value)

    @classmethod
    def course(cls, other_cls: Type[Currency]) -> str:
        result = 1.0
        if cls.__name__ == 'Euro':
            if other_cls.__name__ == 'Pound':
                result = float(cls.pound)
            elif other_cls.__name__ == 'Dollar':
                result = float(cls.usd)

        elif cls.__name__ == 'Pound':
            if other_cls.__name__ == 'Euro':
                result = float(cls.eur / cls.pound)
            elif other_cls.__name__ == 'Dollar':
                result = float(cls.usd / cls.pound)

        elif cls.__name__ == 'Dollar':
            if other_cls.__name__ == 'Euro':
                result = float(cls.eur / cls.usd)
            elif other_cls.__name__ == 'Pound':
                result = float(cls.pound / cls.usd)

        return f"{result} {other_cls.abr} for 1 {cls.abr}"

    def to_currency(self, other_cls: Type[Currency]):
        result = self.value
        if self.abr == 'EUR':
            if other_cls.abr == 'USD':
                result = float(self.value) * self.usd / self.eur
            elif other_cls.abr == 'GBP':
                result = float(self.value) * self.pound / self.eur

        elif self.abr == 'GBP':
            if other_cls.abr == 'EUR':
                result = float(self.value) * self.eur / self.pound
            elif other_cls.abr == 'USD':
                result = float(self.value) * self.usd / self.pound

        elif self.abr == 'USD':
            if other_cls.abr == 'EUR':
                result = float(self.value) * self.eur / self.usd
            elif other_cls.abr == 'GBP':
                result = float(self.value) * self.pound / self.usd

        return other_cls(result)

    def __str__(self):
        return f"{self.value} {self.abr}"

    def __add__(self, other):
        result = self.value + float(str(other.to_currency(self.__class__)).split(' ')[0])

        return self.__class__(result)

    def __gt__(self, other):
        return self.value > other.to_currency(self.__class__).value

    def __lt__(self, other):
        return self.value < other.to_currency(self.__class__).value

    def __eq__(self, other):
        return self.value == other.to_currency(self.__class__).value

class Euro(Currency):
    abr = 'EUR'

    def __init__(self, value):
        super().__init__(value)


class Dollar(Currency):
    abr = 'USD'

    def __init__(self, value):
        super().__init__(value)


class Pound(Currency):
    abr = 'GBP'

    def __init__(self, value):
        super().__init__(value)


if __name__ == '__main__':
    e = Euro(100)
    r = Pound(100)
    d = Dollar(200)
    print(
        f"e + r  =>  {e > r}\n"
        f"r + d  =>  {r < d}\n"
        f"d + e  =>  {d == e}\n"
    )
