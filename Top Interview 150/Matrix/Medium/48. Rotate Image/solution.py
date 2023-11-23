from typing import List


def transpose(matrix: List[List[int]]) -> List[List[int]]:
    """
    Time complexity: O(n^2)
    Space complexity: O(1)
    """
    for row in range(len(matrix)):
        for col in range(row, len(matrix)):
            matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]
    return matrix


def inverse_cols(matrix: List[List[int]]) -> List[List[int]]:
    """
    Time complexity: O(n^2)
    Space complexity: O(1)
    """
    for row in range(len(matrix)):
        for col in range(len(matrix) // 2):
            matrix[row][col], matrix[row][-col - 1] = matrix[row][-col - 1], matrix[row][col]
    return matrix


def rotate_90_degree(matrix: List[List[int]]) -> List[List[int]]:
    """
    Rotation by 90 degree is equivalent to two consecutive operations: transposition and columns inversion/reversion.

    Time complexity: O(n^2)
    Space complexity: O(1)
    """
    return inverse_cols(transpose(matrix))


if __name__ == '__main__':
    input = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    output = [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
    assert rotate_90_degree(input) == output

    input = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
    output = [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]]
    assert rotate_90_degree(input) == output

    assert rotate_90_degree([[1]]) == [[1]]
    assert rotate_90_degree([[1, 2], [3, 4]]) == [[3, 1], [4, 2]]
