from typing import Dict


def get_dict(s: str) -> Dict[str, int]:
    # TODO: Add your code here
    list_of_values = [i for i in s.lower()]
    result = {i: list_of_values.count(i) for i in set(list_of_values)}

    return result


if __name__ == '__main__':
    print(get_dict('Oh, it is python'))


