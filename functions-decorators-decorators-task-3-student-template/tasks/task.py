def validate(fn):
    '''
    Add corresponded arguments and implementation here. 
    '''

    def wrapper(x, y, z):
        if x in range(0, 257) \
                and y in range(0, 257) \
                and z in range(0, 257):
            return fn(x, y, z)
        else:
            return "Function call is not valid!"

    return wrapper


@validate
def set_pixel(x: int, y: int, z: int) -> str:
    return "Pixel created!"


if __name__ == '__main__':
    print(set_pixel(0, 150, 256))
