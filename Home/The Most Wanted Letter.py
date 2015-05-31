__author__ = 'snowwolf'

def checkio(text):
    count = [0] * 26
    text = text.encode('utf-8')
    for x in text:
        if x.isalpha():
            count[ord(x.lower()) - ord('a')] += 1
    maxn = 0
    maxd = 'a'
    for i in range(0, len(count), 1):
        if count[i] > maxn:
            maxn = count[i]
            maxd = chr(ord('a') + i)
    # replace this for solution
    return maxd

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(u"Hello World!") == "l", "Hello test"
    assert checkio(u"How do you do?") == "o", "O is most wanted"
    assert checkio(u"One") == "e", "All letter only once."
    assert checkio(u"Oops!") == "o", "Don't forget about lower case."
    assert checkio(u"AAaooo!!!!") == "a", "Only letters."
    assert checkio(u"abe") == "a", "The First."
    print("Start the long test")
    assert checkio(u"a" * 9000 + u"b" * 1000) == "a", "Long."
    print("The local tests are done.")
