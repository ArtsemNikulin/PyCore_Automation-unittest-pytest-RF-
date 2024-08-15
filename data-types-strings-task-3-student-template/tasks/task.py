def replacer(s: str) -> str:
    """
    Add your code here
    """
    return s.translate({ord('"'): "'", ord("'"): '"'})


if __name__ == '__main__':
    print(replacer('\"\''))
