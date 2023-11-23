from typing import List


def set_zeros(matrix: List[List[int]]):
    """
    Instead of defining sets with null cols and rows, let traverse through elements and set first element of current row
    and col to zero, if current element is equal to zero.
    Then during the second run nullify all elements in col and row if first element is equal to zero.
    The tricky part is that we have to keep track if first row or first column has zero. And firstly treat all elements,
    except first row and first column, and secondly treat first row and first column.

    In the result, we would use constant space.

    Time complexity: O(n*m)
    Space complexity: O(1)
    """
    first_row_has_zero = first_col_has_zero = False
    zero_cnt = 0
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == 0:
                matrix[row][0] = 0
                matrix[0][col] = 0
                if row == 0:
                    first_row_has_zero = True
                if col == 0:
                    first_col_has_zero = True
                zero_cnt += 1

    if zero_cnt > 0:
        for row in range(1, len(matrix)):
            for col in range(1, len(matrix[0])):
                if (matrix[row][0] == 0) or (matrix[0][col] == 0):
                    matrix[row][col] = 0

        if first_row_has_zero:
            for col in range(len(matrix[0])):
                matrix[0][col] = 0
        if first_col_has_zero:
            for row in range(len(matrix)):
                matrix[row][0] = 0


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
