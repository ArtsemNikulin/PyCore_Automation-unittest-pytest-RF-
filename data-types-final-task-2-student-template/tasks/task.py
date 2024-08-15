from typing import List

def check(row_start:int, row_end:int, column_start:int, column_end:int) -> List[List[int]]:
    """
    Add your code here or call it from here   
    """
    result = list()
    rows_range = [i for i in range(row_start, row_end+1)]
    columns_range = [i for i in range(column_start, column_end+1)]
    for i in rows_range:
        multiplication = [j*i for j in columns_range]
        result.append(multiplication)

    return result


if __name__ == '__main__':
    print(check(2,4,3,7))
