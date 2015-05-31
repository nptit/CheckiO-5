__author__ = 'snowwolf'

ONE = ["I", "X", "C", "M"]
FIVE = ["V", "L", "D"]

def checkio(data):
    result = ""
    digits = []
    while data:
        digits.append(data % 10)
        data /= 10
    for i in range(len(digits)):
        if 0 < digits[i] < 4:
            result += ONE[i] * digits[i]
        elif digits[i] == 4:
            result += FIVE[i] + ONE[i]
        elif 4 < digits[i] < 9:
            result += ONE[i] * (digits[i] - 5) + FIVE[i]
        elif digits[i] == 9:
            result += ONE[i+1] + ONE[i]

    # replace this for solution
    return result[::-1]

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(6) == 'VI', '6'
    assert checkio(76) == 'LXXVI', '76'
    assert checkio(499) == 'CDXCIX', '499'
    assert checkio(3888) == 'MMMDCCCLXXXVIII', '3888'