__author__ = 'snowwolf'

# O(2^n)
def break_ring_list(rings, id):
    if len(rings) == 0:
        return 0
    if id > max(reduce(set.union, rings)):
        # impossible
        return 1000000

    t = [x for x in rings if not(id in x)]

    # break the 'id' ring or not
    return min(break_ring_list(rings, id+1), break_ring_list(t, id+1) + 1)

def break_rings(rings):
    print reduce(set.union, rings)
    return break_ring_list(list(rings), 1)

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert break_rings(({1, 2}, {2, 3}, {3, 4}, {4, 5}, {5, 6}, {4, 6})) == 3, "example"
    assert break_rings(({1, 2}, {1, 3}, {1, 4}, {2, 3}, {2, 4}, {3, 4})) == 3, "All to all"
    assert break_rings(({5, 6}, {4, 5}, {3, 4}, {3, 2}, {2, 1}, {1, 6})) == 3, "Chain"
    assert break_rings(({8, 9}, {1, 9}, {1, 2}, {2, 3}, {3, 4}, {4, 5}, {5, 6}, {6, 7}, {8, 7})) == 5, "Long chain"
    assert break_rings(({1, 2}, {2, 3}, {3, 4}, {4, 5}, {5, 2}, {1, 6}, {6, 7}, {7, 8}, {8, 9}, {9, 6},
                        {1, 10}, {10, 11}, {11, 12}, {12, 13}, {13, 10},
                        {1, 14}, {14, 15}, {15, 16}, {16, 17}, {17, 14})) == 8, "tt"