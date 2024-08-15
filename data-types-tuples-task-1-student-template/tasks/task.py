from typing import Tuple


def get_tuple(num: int) -> Tuple[int]:
    # TODO: Add your code here
    result = tuple(int(i) for i in str(num))
    return result


if __name__ == '__main__':
    print(get_tuple(87178291199))
