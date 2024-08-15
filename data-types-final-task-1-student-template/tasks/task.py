from typing import Any, Dict, List, Set


def check(lst: List[Dict[Any, Any]]) -> Set[Any]:
    """
    Add your code here or call it from here   
    """
    result = {list(i.values())[0] for i in lst}
    # result = {''.join(i.values()) for i in lst}
    return result


if __name__ == '__main__':
    print(check([{"V": ""}, {"V": "S002"}]))
