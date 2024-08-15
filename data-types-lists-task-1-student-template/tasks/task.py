from typing import List, Tuple


def sort_unique_elements(str_list: Tuple[str]) -> List[str]:
    # TODO: Add your code here
    final_list = []
    for i in str_list:
        if i not in final_list:
            final_list.append(i)
    final_list.sort()

    return final_list


if __name__ == '__main__':
    print(sort_unique_elements(('red', 'white', 'black', 'red', 'green', 'black')))
