__author__ = 'snowwolf'


def count_gold(pyramid):
    """
    Return max possible sum in a path from top to bottom
    """
    count = [0]
    for line in pyramid:
        count.append(count[-1] + line[-1])
        for i in range(len(line)-1, 0, -1):
            count[i] = max(count[i-1], count[i]) + line[i-1]

    # replace this for solution
    return max(count)


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert count_gold((
        (1,),
        (2, 3),
        (3, 3, 1),
        (3, 1, 5, 4),
        (3, 1, 3, 1, 3),
        (2, 2, 2, 2, 2, 2),
        (5, 6, 4, 5, 6, 4, 3)
    )) == 23, "First example"
    assert count_gold((
        (1,),
        (2, 1),
        (1, 2, 1),
        (1, 2, 1, 1),
        (1, 2, 1, 1, 1),
        (1, 2, 1, 1, 1, 1),
        (1, 2, 1, 1, 1, 1, 9)
    )) == 15, "Second example"
    assert count_gold((
        (9,),
        (2, 2),
        (3, 3, 3),
        (4, 4, 4, 4)
    )) == 18, "Third example"
