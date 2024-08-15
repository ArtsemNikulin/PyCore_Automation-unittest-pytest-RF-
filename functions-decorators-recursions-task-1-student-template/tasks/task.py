from typing import List, Tuple, Union

def seq_sum(sequence: Union[List, Tuple]) -> int:
    """
    Add your code here or call it from here   
    """
    result = int()
    for i in sequence:
        if type(i) == int:
            result+=i
        else:
            result += seq_sum(i)
    return result

if __name__ == '__main__':
    print(seq_sum([1,2,3,[4,5, (6,7)]]))
