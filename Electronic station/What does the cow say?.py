__author__ = 'snowwolf'

import re

COW = r'''
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
'''


def cowsay(text):
    words = re.split(r' *', text)
    lines = []
    line = None
    for word in words:
        if line is None:
            line = word
        elif len(line) + len(word) + 1 > 39:
            lines.append(line)
            line = word
        else:
            line = ' '.join([line, word])
        while len(line) > 39:
            lines.append(line[:39])
            line = line[39:]
    lines.append(line)
    columns = max(map(len, lines))

    ret = r'''
 %s
''' % ('_' * (columns + 2))

    for i, line in enumerate(lines):
        if len(lines) == 1:
            borders = ('<', '>')
        elif i == 0:
            borders = ('/', '\\')
        elif i == len(lines) - 1:
            borders = ('\\', '/')
        else:
            borders = ('|', '|')

        ret += r'''%s %s %s
''' % (borders[0], ''.join([line, ' ' * (columns - len(line))]), borders[1])

    ret += r''' %s''' % ('-' * (columns + 2))

    return ret + COW

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    expected_cowsay_a = r'''
 ____
<  a >
 ----
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
'''

    expected_cowsay_one_line = r'''
 ________________
< Checkio rulezz >
 ----------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
'''
    expected_cowsay_two_lines = r'''
 ________________________________________
/ A                                      \
\ longtextwithonlyonespacetofittwolines. /
 ----------------------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
'''

    expected_cowsay_many_lines = r'''
 _________________________________________
/ Lorem ipsum dolor sit amet, consectetur \
| adipisicing elit, sed do eiusmod tempor |
| incididunt ut labore et dolore magna    |
\ aliqua.                                 /
 -----------------------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
'''
    cowsay_a = cowsay(' a')
    assert cowsay_a == expected_cowsay_a, 'Wrong answer:\n%s' % cowsay_a

    cowsay_one_line = cowsay('Checkio rulezz')
    assert cowsay_one_line == expected_cowsay_one_line, 'Wrong answer:\n%s' % cowsay_one_line

    cowsay_two_lines = cowsay('A longtextwithonlyonespacetofittwolines.')
    assert cowsay_two_lines == expected_cowsay_two_lines, 'Wrong answer:\n%s' % cowsay_two_lines

    cowsay_many_lines = cowsay('Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do '
                                'eiusmod tempor incididunt ut labore et dolore magna aliqua.')
    assert cowsay_many_lines == expected_cowsay_many_lines, 'Wrong answer:\n%s' % cowsay_many_lines
