class Sun:
    _instance = None

    @classmethod
    def inst(cls):
        if cls._instance is None:
            cls._instance = cls.__new__(cls)

        return cls._instance


if __name__ == '__main__':
    p = Sun().inst()
    f = Sun().inst()
    print(p is f)
