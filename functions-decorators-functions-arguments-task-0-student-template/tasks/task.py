from typing import Dict


def generate_squares(num: int) -> Dict[int, int]:
    """
    Add your code here or call it from here   
    """
    squares = {i: i * i for i in range(1, num + 1)}
    return squares


if __name__ == '__main__':
    print(generate_squares(5))
