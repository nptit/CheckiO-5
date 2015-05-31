__author__ = 'snowwolf'


def checkio(number):
    ret = []
    for i in range(9, 1, -1):
        while number % i == 0:
            ret.append(i)
            number /= i
    if number > 1:
        return 0
    return int(''.join(map(str, ret[::-1])))

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(20) == 45, "1st example"
    assert checkio(21) == 37, "2nd example"
    assert checkio(17) == 0, "3rd example"
    assert checkio(33) == 0, "4th example"
    assert checkio(3125) == 55555, "5th example"
    assert checkio(9973) == 0, "6th example"
