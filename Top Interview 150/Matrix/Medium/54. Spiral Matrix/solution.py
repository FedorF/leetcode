from typing import List


def flatten_spirally(matrix: List[List[int]]) -> List[int]:
    """
    Iterate through all elements in matrix, and keep track on left border, right border, upper border, lower border,
    direction in which we're currently moving. If we reach any border, change direction and shrink certain border.
    See image in Readme.md.

    Time complexity: O(m*n)
    Space complexity: O(m*n)
    """
    row = col = 0
    going_across_cols = going_down = going_right = True
    step = 0
    flatten = []
    left_border, right_border = 0, len(matrix[0])-1
    lower_border, upper_border = len(matrix)-1, 0
    while step < len(matrix[0])*len(matrix):  # iterate through all elements in matrix
        flatten.append(matrix[row][col])
        if going_across_cols:
            if going_right:
                if col + 1 > right_border:
                    row += 1
                    going_right = False
                    going_across_cols = False
                    if step >= len(matrix[0]):
                        left_border += 1
                else:
                    col += 1
            else:
                if col - 1 < left_border:
                    row -= 1
                    going_right = True
                    going_across_cols = False
                    right_border -= 1
                else:
                    col -= 1
        else:
            if going_down:
                if row + 1 > lower_border:
                    col -= 1
                    going_down = False
                    going_across_cols = True
                    upper_border += 1
                else:
                    row += 1
            else:
                if row - 1 < upper_border:
                    col += 1
                    going_down = True
                    going_across_cols = True
                    lower_border -= 1
                else:
                    row -= 1
        step += 1

    return flatten


if __name__ == '__main__':
    assert flatten_spirally(matrix=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [1, 2, 3, 6, 9, 8, 7, 4, 5]

    output = [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
    assert flatten_spirally(matrix=[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]) == output
    assert flatten_spirally(matrix=[[1], [2]]) == [1, 2]
    assert flatten_spirally(matrix=[[1, 2]]) == [1, 2]
    assert flatten_spirally(matrix=[[1, 2, 3], [6, 5, 4]]) == [1, 2, 3, 4, 5, 6]

