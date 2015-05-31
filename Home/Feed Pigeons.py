__author__ = 'snowwolf'


def checkio(number):
    minute = 0
    birds = 0
    while True:
        minute += 1
        if number <= birds + minute:
            return max(number, birds)
        birds += minute
        number -= birds

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(1) == 1, "1st example"
    assert checkio(2) == 1, "2nd example"
    assert checkio(5) == 3, "3rd example"
    assert checkio(10) == 6, "4th example"