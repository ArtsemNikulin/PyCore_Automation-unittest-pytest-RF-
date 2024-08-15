from typing import List
import math


def foo(nums: List[int]) -> List[int]:
    # TODO: Add your code here
    final_list = list()
    for i in range(len(nums)):
        list_for_calculation = nums[:i] + nums[i + 1:]
        final_list.append(math.prod(list_for_calculation))

    return final_list


if __name__ == '__main__':
    print(foo([5, 6, 7]))
