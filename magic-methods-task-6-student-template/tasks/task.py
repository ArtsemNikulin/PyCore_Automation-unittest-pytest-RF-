import os


class Cd:
    def __init__(self, path):
        if os.path.exists(os.getcwd() + path) and os.path.isdir(os.getcwd() + path):
            self.path = path
        else:
            raise ValueError(f"folder '{path}' does not exist")

    def __enter__(self):
        self.__current_path = os.getcwd()
        os.chdir(os.getcwd() + self.path)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        os.chdir(self.__current_path)


if __name__ == '__main__':
    # print(os.getcwd())
    with Cd('/test/test2') as f:
    #     print(os.getcwd())
    # print(os.getcwd())
        pass
