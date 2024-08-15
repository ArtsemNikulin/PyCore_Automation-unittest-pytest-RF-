import string
from typing import List


def split(data: str, sep=None, maxsplit=-1):
    result = []
    if len(data) == 0:
        return result

    if data.startswith(' '):
        for i, val in enumerate(data):
            if val != ' ':
                data = data[i:]
                break
    if sep is None:
        sep = ' '

    if maxsplit == 0:
        return [data]
    elif maxsplit == -1:
        paste_part = ''
        for i in range(len(data)):
            if data[i] != sep:
                paste_part += data[i]
                if i == len(data) - 1:
                    result.append(paste_part)
            elif data[i] == sep and paste_part == '':
                result.append('')
            elif data[i] == sep and paste_part != '':
                result.append(paste_part)
                paste_part = ''
                if i == len(data) - 1:
                    result.append('')
        if sep == ' ':
            result = [i for i in result if i != '']

    elif maxsplit > 0:
        counter = 0
        for i in range(len(data)):
            if data[i] == sep:
                result.append(data[:i])
                tail = [i for i in data[i + 1:]]
                counter += 1
                if counter == maxsplit:
                    break

        for i, val in enumerate(tail):
            if val != ' ':
                tail = ''.join(tail[i:])
                break
        result.append(tail)

    return result


if __name__ == '__main__':
    split('  asd')
