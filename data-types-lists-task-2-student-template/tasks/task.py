from typing import Union, List

ListType = List[Union[int, str]]


def get_fizzbuzz_list(n: int) -> ListType:
    # TODO: Add your code here
    final_list = list()
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            final_list.append('FizzBuzz')
        elif i % 3 == 0 and i % 5 != 0:
            final_list.append('Fizz')
        elif i % 3 != 0 and i % 5 == 0:
            final_list.append('Buzz')
        else:
            final_list.append(i)

    return final_list


if __name__ == '__main__':
    print(get_fizzbuzz_list(15))