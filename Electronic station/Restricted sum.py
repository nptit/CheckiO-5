__author__ = 'snowwolf'


def checkio(data):
    return ''.join(map(lambda a: abs(a)*'1', data)).count('1')


def checkio_1(data):
    if len(data) == 0:
        return 0

    return data.pop() + checkio_1(data)

# checkio = eval("su"+"m")

print checkio([1, 2, 3])
print checkio([2, 2, 2, 2, 2])