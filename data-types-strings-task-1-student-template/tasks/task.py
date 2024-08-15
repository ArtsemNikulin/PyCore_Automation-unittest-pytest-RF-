def get_fractions(a_b: str, c_b: str) -> str:
    """
    Add your code here  
    """
    first_fraction = tuple(a_b.split('/'))
    second_fraction = tuple(c_b.split('/'))

    return f'{a_b} + {c_b} = {int(first_fraction[0]) + int(second_fraction[0])}/{second_fraction[1]}'

if __name__ == '__main__':
    print(get_fractions('1/3', '5/3'))