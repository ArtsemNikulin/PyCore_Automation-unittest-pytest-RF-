from typing import Union

def divide(str_with_ints: str) -> Union[float, str]:
    """
    Returns the result of dividing two numbers or an error message.
    :arg
        str_with_ints: str, ex. "4 2";
    :return
        result of dividing: float, ex. 2.0 (4 / 2 = 2.0);
        error response in "Error code: {error message}: str;
    """
    try:
        ints = [int(i) for i in str_with_ints.split(' ') if i != '']
        return ints[0] / ints[1]
    except ValueError as error_message:
        return f'Error code: {error_message}'
    except ZeroDivisionError as error_message:
        return (f'Error code: {error_message}')


if __name__ == '__main__':
    print(divide('4   0'))
