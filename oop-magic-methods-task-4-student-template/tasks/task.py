class PriceControl:
    """
    Descriptor which don't allow to set price
    less than 0 and more than 100 included.
    """

    def __init__(self, default_value=None):
        self._value = default_value

    def __get__(self, instance, owner):
        return self._value

    def __set__(self, instance, value):
        if 0 > value or value > 100:
            raise ValueError("Price must be between 0 and 100")
        self._value = value


class NameControl:
    """
    Descriptor which don't allow to change field value after initialization.
    """

    def __init__(self, atr, default_value=None):
        self._value = default_value
        self._atr = atr

    def __get__(self, instance, owner):
        return self._value

    def __set__(self, instance, value):
        if self._value is not None:
            raise ValueError(f"{self._atr} can not be changed.")
        self._value = value


class Book:
    author = NameControl('Author')
    name = NameControl('Name')
    price = PriceControl()

    def __init__(self, book_author, book_name, book_price):
        self.name = book_name
        self.author = book_author
        self.price = book_price


if __name__ == '__main__':
    b = Book("William Faulkner", "The Sound and the Fury", 12)
    print(f"Author='{b.author}', Name='{b.name}', Price='{b.price}'")
    b.price = 55
    print(b.price)
    b.price = -12
    b.price = 101
    b.author = "new author"
    b.name = "new name"

