__author__ = 'snowwolf'

import itertools as it
import operator as op
import re
import string


def subchr(text1, text2, alphabet=string.ascii_uppercase):
    seq1, seq2 = [map(alphabet.index, t) for t in (text1, text2)]
    return ''.join(alphabet[i] for i in [op.sub(x, seq2[j % len(seq2)]) for j, x in enumerate(seq1)])
#   Python 3
#   return ''.join(alphabet[i] for i in map(op.sub, seq1, it.cycle(seq2)))


def decode_vigenere1(old_decrypted, old_encrypted, new_encrypted):
    keyword = subchr(old_encrypted, old_decrypted)
    # match = re.match(r'(?P<repeat>.+)(?P=repeat)|(?P<whole>.+)', keyword)
    # print keyword, match.group('repeat') or match.group('whole')
    # return subchr(new_encrypted, match.group('repeat') or match.group('whole'))
    match = re.match(r'(.+)(\1)|(.+)', keyword)
    return subchr(new_encrypted, match.group(1) or match.group(3))


def decode_vigenere(old_decrypted, old_encrypted, new_encrypted):
    return decode_vigenere1(old_decrypted, old_encrypted, new_encrypted)
    key = []
    ret = []
    for i in range(len(old_encrypted)):
        x, y = ord(old_decrypted[i]), ord(old_encrypted[i])
        k = y - x
        key.append(k if k >= 0 else k + 26)

    if len(new_encrypted) > len(old_encrypted):
        for klen in range(len(key) / 2, 0, -1):
            for i in range(klen):
                if key[i] != key[i + klen]:
                    break
            else:
                key = key[:klen]
                break

    for i, x in enumerate(new_encrypted):
        r = ord(x) - ord('A') - key[i % len(key)]
        if r < 0:
            r += 26
        ret.append(chr(ord('A') + r))

    return ''.join(ret)

# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert decode_vigenere(u'DONTWORRYBEHAPPY',
                           u'FVRVGWFTFFGRIDRF',
                           u'DLLCZXMFVRVGWFTF') == "BEHAPPYDONTWORRY", "CHECKIO"
    assert decode_vigenere(u'HELLO', u'OIWWC', u'ICP') == "BYE", "HELLO"
    assert decode_vigenere(u'LOREMIPSUM',
                           u'OCCSDQJEXA',
                           u'OCCSDQJEXA') == "LOREMIPSUM", "DOLORIUM"
    assert decode_vigenere(u'HEHE', u'OIOI', u'ICICICIC') == "BYBYBYBY", "HELLO"
