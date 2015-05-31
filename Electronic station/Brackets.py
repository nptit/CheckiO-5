__author__ = 'snowwolf'


def checkio(expression):
    ret = True
    brackets = ('(', ')', '[', ']', '{', '}')
    stack = []

    for x in expression:
        # found = [i for (i, a) in enumerate(brackets) if a == x]
        # if not found:
        #     continue
        #
        # k = found[0]
        if x not in brackets:
            continue
        k = brackets.index(x)
        if k % 2 == 0:
            stack.append(k)
        elif len(stack) and k == stack[-1] + 1:
            stack.pop()
        else:
            ret = False
            break

    if len(stack):
        ret = False

    return ret

# another way to define dict
BRACKET_PAIRS = ['()', '{}', '[]', '<>']
OPEN_BRACKETS = {a for a, _ in BRACKET_PAIRS}
CLOSE_BRACKETS = {b: a for a, b in BRACKET_PAIRS}


def checkio_use_dict(data):
    stack = [""]
    brackets = {"(":")","[":"]","{":"}"}
    for c in data:
        if c in brackets:
            stack.append(brackets[c])
        elif c in brackets.values() and c != stack.pop():
            return False
    return stack == [""]

#  "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(u"((5+3)*2+1)") == True, "Simple"
    assert checkio(u"{[(3+1)+2]+}") == True, "Different types"
    assert checkio(u"(3+{1-1)}") == False, ") is alone inside {}"
    assert checkio(u"[1+1]+(2*2)-{3/3}") == True, "Different operators"
    assert checkio(u"(({[(((1)-2)+3)-3]/3}-3)") == False, "One is redundant"
    assert checkio(u"2+3") == True, "No brackets, no problem"
    assert checkio_use_dict(u")") == False, "My test"
