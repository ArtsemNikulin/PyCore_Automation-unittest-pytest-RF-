class Counter:
    def __init__(self, start = 0, stop=None):
        self.start = start
        self.stop = stop

    def increment(self):
        if self.stop is None or self.start < self.stop:
            self.start +=1
        else:
            print("Maximal value is reached.")

    def get(self):
        return self.start



if __name__ == '__main__':
    c = Counter(start=42, stop=43)
    c.increment()
    print(c.get())
    c.increment()
    print(c.get())




