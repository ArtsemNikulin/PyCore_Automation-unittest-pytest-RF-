from typing import Any, List

def linear_seq(sequence: List[Any]) -> List[Any]:
    """
    Add your code here or call it from here   
    """
    result = []
    for i in sequence:
        if type(i) == int:
            result.append(i)
        else:
            for j in linear_seq(i):
                result.append(j)

    return result


if __name__ == '__main__':
    sequence = [1, 2, 3, [4, 5, (6, 7)]]
    print(linear_seq(sequence))
