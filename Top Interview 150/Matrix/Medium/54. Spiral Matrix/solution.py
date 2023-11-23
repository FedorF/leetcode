from typing import List


def flatten_spirally(matrix: List[List[int]]) -> List[int]:
    """
    Iterate through all elements in matrix, and keep track on left border, right border, upper border, lower border,
    direction in which we're currently moving. If we reach any border, change direction and shrink certain border.
    (See image in Readme.md)

    Time complexity: O(m*n)
    Space complexity: O(m*n)
    """
    step = row = col = 0
    traverse_horizontally = going_down = going_right = True
    left_border, right_border = 0, len(matrix[0]) - 1
    lower_border, upper_border = len(matrix) - 1, 0
    result = []
    while step < len(matrix[0]) * len(matrix):
        result.append(matrix[row][col])
        if traverse_horizontally:
            if going_right:
                if col + 1 > right_border:  # we reached right border, so switch direction to down-wise
                    row += 1
                    going_right = False
                    traverse_horizontally = False
                    if step >= len(matrix[0]):
                        left_border += 1
                else:  # continue moving from left to right
                    col += 1
            else:
                if col - 1 < left_border:  # we reached left border, so switch direction to up-wise
                    row -= 1
                    going_right = True
                    traverse_horizontally = False
                    right_border -= 1
                else:  # continue moving from right to left
                    col -= 1
        else:
            if going_down:
                if row + 1 > lower_border:  # we reached lower border, so switch direction to left-wise
                    col -= 1
                    going_down = False
                    traverse_horizontally = True
                    upper_border += 1
                else:  # continue moving down-wise
                    row += 1
            else:
                if row - 1 < upper_border:  # we reached upper border, so switch direction to right-wise
                    col += 1
                    going_down = True
                    traverse_horizontally = True
                    lower_border -= 1
                else:  # continue moving up-wise
                    row -= 1
        step += 1  # update step variable

    return result


if __name__ == '__main__':
    assert flatten_spirally(matrix=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [1, 2, 3, 6, 9, 8, 7, 4, 5]

    output = [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
    assert flatten_spirally(matrix=[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]) == output
    assert flatten_spirally(matrix=[[1], [2]]) == [1, 2]
    assert flatten_spirally(matrix=[[1, 2]]) == [1, 2]
    assert flatten_spirally(matrix=[[1, 2, 3], [6, 5, 4]]) == [1, 2, 3, 4, 5, 6]
