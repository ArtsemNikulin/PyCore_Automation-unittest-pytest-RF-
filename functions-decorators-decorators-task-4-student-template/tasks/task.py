
def decorator_apply(lambda_func):
    '''
    Add your implementation here
    '''
    def wrapper(num):
        return lambda_func

    return wrapper

@decorator_apply(lambda user_id: user_id + 1)
def return_user_id(num: int) ->int:
    return num


if __name__ == '__main__':
    print(return_user_id(42))