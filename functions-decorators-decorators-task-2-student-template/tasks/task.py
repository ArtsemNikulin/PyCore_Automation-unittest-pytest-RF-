import time
import string


def log(fn):
    """
    Add your code here or call it from here   
    """

    def wrapper(*args, **kwargs):
        start = time.time()
        alphabet = string.ascii_lowercase
        kwargs = ', '.join([f'{i}={j}' for i, j in kwargs.items()])
        args = ', '.join([f'{i}={j}' for i, j in dict(zip([i for i in alphabet[:len(args)]], args)).items()])
        with open('log.txt', 'w') as f:
            f.write(f'{fn.__name__}; args: {args}; kwargs: {kwargs}; execution time: {time.time() - start} sec.')

    return wrapper


@log
def foo(*args, **kwargs):
    pass


if __name__ == '__main__':
    foo(1, 2, 3, c=5, d=5)
