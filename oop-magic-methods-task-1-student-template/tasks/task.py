from typing import List


class Counter:
    def __init__(self, values: List[int]):
        self.values = values


    def __add__(self, other):
        result = [f"{i} {other}" for i in self.values]
        return result


if __name__ == '__main__':
    obj = Counter([1, 2, 3]) + "mississippi"
    print(obj)
