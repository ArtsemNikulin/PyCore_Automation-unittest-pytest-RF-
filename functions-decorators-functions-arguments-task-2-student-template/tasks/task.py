def union(*args) -> set:
    result = set()
    for arg in args:
        for val in arg:
            result.add(val)

    return result


def intersect(*args) -> set:
    result = set()
    for arg in args:
        for val in arg:
            if all(val in arg for arg in args):
                result.add(val)

    return result


if __name__ == '__main__':
    print(intersect(('S', 'A', 'C'), ('P', 'C', 'S'), ('G', 'H', 'S', 'C')))
    print(union(('S', 'A', 'M'), ['S', 'P', 'A', 'C']))