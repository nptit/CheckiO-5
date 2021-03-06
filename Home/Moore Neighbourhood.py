__author__ = 'snowwolf'


def count_neighbours(grid, row, col):
    neighbours = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))

    def check_inside(x, y):
        return 0 <= x < len(grid) and 0 <= y < len(grid[0])

    return sum([grid[row + x][col + y] for x, y in neighbours if check_inside(row + x, col + y)])


#     rows = range(max(0, row - 1), min(row + 2, len(grid)))
#     cols = range(max(0, col - 1), min(col + 2, len(grid[0])))
# ​
#     return sum(grid[r][c] for r in rows for c in cols) - grid[row][col]


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert count_neighbours(
        ((1, 0, 0, 1, 0),
         (0, 1, 0, 0, 0),
         (0, 0, 1, 0, 1),
         (1, 0, 0, 0, 0),
         (0, 0, 1, 0, 0),), 1, 2) == 3, "1st example"
    assert count_neighbours(((1, 0, 0, 1, 0),
                             (0, 1, 0, 0, 0),
                             (0, 0, 1, 0, 1),
                             (1, 0, 0, 0, 0),
                             (0, 0, 1, 0, 0),), 0, 0) == 1, "2nd example"
    assert count_neighbours(((1, 1, 1),
                             (1, 1, 1),
                             (1, 1, 1),), 0, 2) == 3, "Dense corner"
    assert count_neighbours(((0, 0, 0),
                             (0, 1, 0),
                             (0, 0, 0),), 1, 1) == 0, "Single"
