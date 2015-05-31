__author__ = 'snowwolf'

# checkio = lambda s: not(
#         len(s) < 10
#         or s.isdigit()
#         or s.isalpha()
#         or s.islower()
#         or s.isupper()
#     )

def checkio(data):
    if len(data) < 10:
        return False
    hasDigit = False
    hasUpper = False
    hasLower = False
    for x in data:
        hasDigit = hasDigit or x.isdigit()
        hasUpper = hasUpper or x.isupper()
        hasLower = hasLower or x.islower()
    # replace this for solution
    return hasDigit and hasUpper and hasLower

# Some hints
# Just check all conditions


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(u'A1213pokl') == False, "1st example"
    assert checkio(u'bAse730onE4') == True, "2nd example"
    assert checkio(u'asasasasasasasaas') == False, "3rd example"
    assert checkio(u'QWERTYqwerty') == False, "4th example"
    assert checkio(u'123456123456') == False, "5th example"
    assert checkio(u'QwErTy911poqqqq') == True, "6th example"
    assert checkio(u'!1234567890') == True, "7th example"

