from typing import List


def split_by_index(s: str, indexes: List[int]) -> List[str]:
    """
    Add your code here or call it from here   
    """
    indexes.insert(0, 0)
    slices = {indexes[i]: indexes[i + 1] if len(indexes[i:i + 2]) > 1 else None for i in range(len(indexes))}

    result = [s[k:v] for k, v in slices.items()]
    if '' in result:
        result.remove('')
    return result


if __name__ == '__main__':
    print(split_by_index("pythoniscool,isn'tit?", [6, 8, 12, 13, 18]))
