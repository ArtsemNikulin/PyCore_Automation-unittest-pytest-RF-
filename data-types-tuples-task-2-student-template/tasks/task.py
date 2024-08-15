from typing import Any, Tuple, List


def get_pairs(lst: List[Any]) -> List[Tuple[Any, ...]]:
    # TODO: Add your code here
    result = [tuple(lst[i:i + 2]) for i in range(len(lst)) if len(lst[i:i + 2]) > 1]

    return result


if __name__ == '__main__':
    print(get_pairs(['need', 'to', 'sleep', 'more']))
