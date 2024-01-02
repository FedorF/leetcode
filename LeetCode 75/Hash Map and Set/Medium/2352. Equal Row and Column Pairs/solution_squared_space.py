from collections import Counter
from typing import List


def find_difference(grid: List[int]) -> int:
    """
    Define two lists: one - for rows, another - for cols.
    Fill lists transforming elements to string, in order to build counter of rows ana columns.
    In the end, calculate pairs row-col tha are equal.


    Time complexity: O(n^2)
    Space complexity: O(n^2)

    """
    n = len(grid)
    rows, cols = ["" for _ in range(n)], ["" for _ in range(n)]
    for row_ind in range(n):  # build lists with rows and cols
        for col_ind in range(n):
            x = grid[row_ind][col_ind]
            rows[row_ind] += f" {x}"
            cols[col_ind] += f" {x}"

    res = 0
    rows_cnt = Counter(rows)
    for col in cols:  # count pairs
        if col in rows_cnt:
            res += rows_cnt[col]

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
