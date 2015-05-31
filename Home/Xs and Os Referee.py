__author__ = 'snowwolf'


def checkio(game_result):
    for i in range(3):
        game_result.append("".join([game_result[x][i] for x in range(3)]))
    game_result.append(game_result[0][0] + game_result[1][1] + game_result[2][2])
    game_result.append(game_result[0][2] + game_result[1][1] + game_result[2][0])
    for s in game_result:
        if s == u"XXX":
            return "X"
        elif s == u"OOO":
            return "O"
    return "D"

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        u"X.O",
        u"XX.",
        u"XOO"]) == "X", "Xs wins"
    assert checkio([
        u"OO.",
        u"XOX",
        u"XOX"]) == "O", "Os wins"
    assert checkio([
        u"OOX",
        u"XXO",
        u"OXX"]) == "D", "Draw"
    assert checkio([
        u"O.X",
        u"XX.",
        u"XOO"]) == "X", "Xs wins again"

