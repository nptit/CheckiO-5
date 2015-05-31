__author__ = 'snowwolf'

# Your optional code here
# You can import some modules or create additional functions


def checkio(data):
    # Your code here
    # It's main function. Don't remove this function
    # It's used for auto-testing and must return a result for check.  
    d = {}
    for x in data:
        if x in d:
            d[x] += 1
        else:
            d[x] = 1

    data = [x for x in data if d[x] > 1]
    # data = filter(lambda x: d[x] > 1, data)
    # for i in range(len(data)-1, -1, -1):
    #     if d[data[i]] == 1:
    #         del data[i]
    # replace this for solution
    return data

# Some hints
# You can use list.count(element) method for counting.
# Create new list with non-unique elements
# Loop over original list


if __name__ == "__main__":
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert isinstance(checkio([1]), list), "The result must be a list"
    assert checkio([1, 2, 3, 1, 3]) == [1, 3, 1, 3], "1st example"
    assert checkio([1, 2, 3, 4, 5]) == [], "2nd example"
    assert checkio([5, 5, 5, 5, 5]) == [5, 5, 5, 5, 5], "3rd example"
    assert checkio([10, 9, 10, 10, 9, 8]) == [10, 9, 10, 10, 9], "4th example"
