__author__ = 'snowwolf'


def letter_queue(commands):
    letters = []
    for x in commands:
        arr = x.split()
        if arr[0] == "PUSH":
            letters.append(arr[1])
        elif letters:
            del letters[0]
    return "".join(letters)

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert letter_queue(["PUSH A", "POP", "POP", "PUSH Z", "PUSH D", "PUSH O", "POP", "PUSH T"]) == "DOT", "dot example"
    assert letter_queue(["POP", "POP"]) == "", "Pop, Pop, empty"
    assert letter_queue(["PUSH H", "PUSH I"]) == "HI", "Hi!"
    assert letter_queue([]) == "", "Nothing"
