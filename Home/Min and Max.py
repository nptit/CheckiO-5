__author__ = 'snowwolf'


def min(*args, **kwargs):
    key = kwargs.get("key", None)
    l = args if len(args) > 1 else args[0]
    ret = None
    for x in l:
        if (ret is None) or \
                (key is not None and key(x) < key(ret)) or \
                (key is None and x < ret):
            ret = x

    return ret


def max(*args, **kwargs):
    key = kwargs.get("key", None)
    l = args if len(args) > 1 else args[0]
    ret = None
    for x in l:
        if (ret is None) or \
                (key is not None and key(x) > key(ret)) or \
                (key is None and x > ret):
            ret = x

    # key = kwargs.get("key", lambda x: x)
    # args = args[0]
    # args = iter(args)
    # ret = next(args)
    return ret


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert max(3, 2) == 3, "Simple case max"
    assert min(3, 2) == 2, "Simple case min"
    assert max([1, 2, 0, 3, 4]) == 4, "From a list"
    assert min("hello") == "e", "From string"
    assert max(2.2, 5.6, 5.9, key=int) == 5.6, "Two maximal items"
    assert min([[1, 2], [3, 4], [9, 0]], key=lambda x: x[1]) == [9, 0], "lambda key"
