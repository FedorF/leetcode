from collections import Counter
from typing import List


def find_difference(grid: List[int]) -> int:
    """
    Build counter dict for rows transformed to string. Run through columns and check if column is equal any key from
    rows counter. If so, add value for the key to the resulted variable.

    Now, we store only n rows, therefore linear space

    Time complexity: O(n^2)
    Space complexity: O(n)

    """
    n = len(grid)
    rows = {}
    for row in grid:
        s = str(row)
        if s in rows:
            rows[s] += 1
        else:
            rows[s] = 1

    res = 0
    for col_ind in range(n):
        col = []
        for row_ind in range(n):
            col.append(grid[row_ind][col_ind])
        res += rows.get(str(col), 0)

    return res


if __name__ == '__main__':
    actual, expected = find_difference(grid=[[11, 1], [1, 11]]), 2
    assert actual == expected, f"actual: {actual}, expected: {expected}"

    actual, expected = find_difference(grid=[[3, 2, 1], [1, 7, 6], [2, 7, 7]]), 1
    assert actual == expected, f"actual: {actual}, expected: {expected}"

    actual, expected = find_difference([[3, 1, 2, 2], [1, 4, 4, 5], [2, 4, 2, 2], [2, 4, 2, 2]]), 3
    assert actual == expected, f"actual: {actual}, expected: {expected}"

    actual, expected = find_difference([[1]]), 1
    assert actual == expected, f"actual: {actual}, expected: {expected}"

    actual, expected = find_difference([[1, 1], [1, 1]]), 4
    assert actual == expected, f"actual: {actual}, expected: {expected}"
