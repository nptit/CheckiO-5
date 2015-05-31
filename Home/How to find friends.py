__author__ = 'snowwolf'


def check_connection(network, first, second):
    network = [x.split('-') for x in network]
    connected = []
    new = [first]
    while new:
        current = new.pop()
        if current == second:
            return True
        connected.append(current)
        for x in network:
            friend = [y for y in x if y != current]
            if len(friend) == 1 and friend[0] not in connected and friend[0] not in new:
                new.append(friend[0])
    return False


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "scout2", "scout3") == True, "Scout Brotherhood"
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "super", "scout2") == True, "Super Scout"
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "dr101", "sscout") == False, "I don't know any scouts."
