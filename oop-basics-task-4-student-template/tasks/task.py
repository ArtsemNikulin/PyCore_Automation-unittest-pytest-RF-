class HistoryDict:
    def __init__(self, value):
        self.value = value
        self.history = list()

    def set_value(self, key, val):
        if key not in self.history:
            self.history.append(key)
        self.value = {key: val}
        self.history = self.history[-5:]

    def get_history(self):
        return self.history


if __name__ == '__main__':
    obj = HistoryDict({'a': 1})
    # obj.set_value('a', 2)
    obj.set_value('c', 2)
    obj.set_value('c', 2)
    obj.set_value('n', 2)
    obj.set_value('u', 2)
    obj.set_value('v', 3)
    obj.set_value('v', 3)
    obj.set_value('m', 3)
    print(obj.value)
    print(obj.get_history())
