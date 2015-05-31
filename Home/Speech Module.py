__author__ = 'snowwolf'

FIRST_TEN = ["one", "two", "three", "four", "five", "six", "seven",
             "eight", "nine"]
SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
              "sixteen", "seventeen", "eighteen", "nineteen"]
OTHER_TENS = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy",
              "eighty", "ninety"]
HUNDRED = "hundred"


def checkio(number):
    words = []
    h = number / 100
    if h > 0:
        words.append(FIRST_TEN[h-1] + " " + HUNDRED)
    number %= 100
    t = number / 10
    if t > 1:
        words.append(OTHER_TENS[t-2])
        number %= 10
    if number >= 10:
        words.append(SECOND_TEN[number % 10])
    elif number > 0:
        words.append(FIRST_TEN[number-1])
    # replace this for solution
    return " ".join(x for x in words)

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(4) == 'four', "1st example"
    assert checkio(133) == 'one hundred thirty three', "2nd example"
    assert checkio(12) == 'twelve', "3rd example"
    assert checkio(101) == 'one hundred one', "4th example"
    assert checkio(212) == 'two hundred twelve', "5th example"
    assert checkio(40) == 'forty', "6th example"
    assert not checkio(212).endswith(' '), "Don't forget strip whitespaces at the end of string"
