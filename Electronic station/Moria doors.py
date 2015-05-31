__author__ = 'snowwolf'

import re


def words_likeness(a, b):
    likeness = 0
    if a[0] == b[0]:
        likeness += 10
    if a[-1] == b[-1]:
        likeness += 10
    likeness += float(min(len(a), len(b))) / max(len(a), len(b)) * 30
    likeness += float(len(set(a) & set(b))) / len(set(a) | set(b)) * 50
    return likeness


def find_word(message):
    message = message.lower()
    words = re.findall('[a-z]+', message)
    words.reverse()
    return max(words, key=lambda a: sum((words_likeness(a, b) for b in words)))
    # return max(words, key=lambda a: sum(map(words_likeness, words, [a] * len(words))))

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert find_word(u"Speak friend and enter.") == "friend", "Friend"
    assert find_word(u"Beard and Bread") == "bread", "Bread is Beard"
    assert find_word(u"The Doors of Durin, Lord of Moria. Speak friend and enter. "
                     u"I Narvi made them. Celebrimbor of Hollin drew these signs") == "durin", "Durin"
    assert find_word(u"Aoccdrnig to a rscheearch at Cmabrigde Uinervtisy."
                     u" According to a researcher at Cambridge University.") == "according", "Research"
    assert find_word(u"One, two, two, three, three, three.") == "three", "Repeating"
