def get_longest_word(s: str) -> str:
    """
     Add your code here 
    """
    s = s.split()
    s.sort(reverse=True, key=len)

    return s[0]


if __name__ == '__main__':
    print(get_longest_word('Python is simple and effective!'))
