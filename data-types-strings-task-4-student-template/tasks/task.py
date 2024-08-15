def check_str(s: str):
    """
    Add your code here
    """
    s = ''.join(char.lower() if char.isalnum() else '' for char in s)
    if s[::-1] == s:
        return True
    else:
        return False

if __name__ == '__main__':
    print(check_str("No 'x' in Nixon"))