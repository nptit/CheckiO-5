__author__ = 'snowwolf'


def golf(x):
    while x:
        x += 1
        b = str(x)
        if not ([i for i in range(len(b)) if b[i] != b[-i-1]] or [y for y in range(2, x/2) if not x % y]):
            return x

if __name__ == "__main__":
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert golf(2) == 3, "1st example"
    assert golf(13) == 101, "2nd example"
    assert golf(101) == 131, "3rd example"