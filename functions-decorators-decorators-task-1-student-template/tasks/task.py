from typing import Dict
import time

execution_time: Dict[str, float] = {}


def time_decorator(fn):
    """
    Create a decorator function `time_decorator`
    which has to calculate decorated function execution time
    and put this time value to `execution_time` dictionary where `key` is
    decorated function name and `value` is this function execution time.
    """

    def wrapper(a, b, sleep_time):
        start = time.time()
        result = fn(a, b, sleep_time)
        execution_time[fn.__name__] = time.time() - start
        return result

    return wrapper


@time_decorator
def func_add(a, b, sleep_time):
    time.sleep(sleep_time)
    return a + b


if __name__ == '__main__':
    print(func_add(1, 2, 3))
    print(execution_time['func_add'])
