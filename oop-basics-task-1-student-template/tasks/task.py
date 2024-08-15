class Field:
    __value = None

    def __init__(self):
        self.__value = None

    # TODO: add your code here
    def get_value(self):
        return self.__value

    def set_value(self, val):
        self.__value = val


if __name__ == '__main__':
    obj = Field()
    print(obj.get_value())
    obj.set_value('a')
    print(obj.get_value())
