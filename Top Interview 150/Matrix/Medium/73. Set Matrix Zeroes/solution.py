from typing import List


def set_zeros(matrix: List[List[int]]):
    """
    Traverse through the elements and save row and col in defined set, if element is equal to zero.
    Make a second run and nullify all corresponding elements using sets.

    Time complexity: O(n*m)
    Space complexity: O(m+n) due to we're keeping rows and cols
    """
    zero_rows, zero_cols = set(), set()
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == 0:
                zero_rows.add(row)
                zero_cols.add(col)

    if len(zero_cols) > 0 or len(zero_rows) > 0:
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if row in zero_rows or col in zero_cols:
                    matrix[row][col] = 0


if __name__ == '__main__':
    input = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    set_zeros(input)
    assert input == [[1, 0, 1], [0, 0, 0], [1, 0, 1]]

    input = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
    set_zeros(input)
    assert input == [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]

    input = [[1, 1, 2, 10]]
    set_zeros(input)
    assert input == [[1, 1, 2, 10]]

    input = [[1, 1, 2, 0]]
    set_zeros(input)
    assert input == [[0, 0, 0, 0]]

    input = [[1], [2], [3]]
    set_zeros(input)
    assert input == [[1], [2], [3]]

    input = [[0], [2], [3]]
    set_zeros(input)
    assert input == [[0], [0], [0]]
