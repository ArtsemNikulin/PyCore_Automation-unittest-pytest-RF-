from typing import List, Dict


def combine_dicts(*args: List[Dict[str, int]]) -> Dict[str, int]:
    result = dict()
    for item in args:
        for key, values in item.items():
            if result.get(key) is None:
                result[key] = values
            else:
                result[key] += values

    return result


if __name__ == '__main__':
    dict_1 = {'a': 100, 'b': 200}
    dict_2 = {'a': 200, 'c': 300}
    dict_3 = {'a': 300, 'd': 100}
    print(combine_dicts(dict_1, dict_2,dict_3))
