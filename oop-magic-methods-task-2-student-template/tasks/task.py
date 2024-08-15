class Bird:
    def __init__(self, name):
        self.name = name

    def walk(self):
        return self.name + ' bird can walk'

    def fly(self):
        return self.name + ' can walk'

    def __str__(self):
        return f"{self.name} bird can walk and fly"


class FlyingBird:
    def __init__(self, name, ration='grains'):
        self.name = name
        self.ration = ration

    def walk(self):
        return self.name + ' can walk'

    def fly(self):
        return self.name + ' can walk'

    def eat(self):
        return 'It eats mostly ' + self.ration

    def __str__(self):
        return f"{self.name} bird can walk and fly"


class NonFlyingBird:
    def __init__(self, name, ration='fish'):
        self.name = name
        self.ration = ration

    def walk(self):
        return self.name + ' can walk'

    def swim(self):
        return self.name + ' bird can swim'

    def eat(self):
        return 'It eats mostly ' + self.ration

    def __str__(self):
        return f"{self.name} bird can walk and swim"


class SuperBird(NonFlyingBird):
    def __init__(self, name):
        super().__init__(name)
        self.name = name

    def __str__(self):
        return f"{self.name} bird can walk, swim and fly"


if __name__ == '__main__':
    obj = Bird("Any")
    print(obj.walk())
    p = NonFlyingBird("Penguin", "fish")
    print(p.swim())
    # print(p.fly())
    print(p.eat())
    c = FlyingBird("Canary")
    print(str(c))
    print(c.eat())
    s = SuperBird("Gull")
    print(str(s))
    print(s.eat())
