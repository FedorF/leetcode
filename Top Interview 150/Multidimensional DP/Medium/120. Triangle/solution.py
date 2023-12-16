import math
from typing import List


def calc_min_path_sum(triangle: List[List[int]]) -> int:
    """
    DP approach (bottom-up). Start with base case (first element), and continue calculations using previous min paths.

    Time complexity: O(n^2)
    Space complexity: O(1), due to in-place calculations
    """
    if len(triangle) == 1:
        return triangle[0][0]

    global_min = math.inf
    for row in range(1, len(triangle)):
        for i in range(len(triangle[row])):
            if i == 0:
                triangle[row][i] += triangle[row - 1][i]

            elif i == len(triangle[row]) - 1:
                triangle[row][i] += triangle[row - 1][-1]

            else:
                triangle[row][i] += min(triangle[row - 1][i], triangle[row - 1][i - 1])

            if row == len(triangle) - 1:  # if last row, start min path search
                global_min = min(global_min, triangle[row][i])

    return global_min


if __name__ == '__main__':
    assert calc_min_path_sum(triangle=[[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]) == 11
    assert calc_min_path_sum(triangle=[[-11]]) == -11
    assert calc_min_path_sum(triangle=[[-1], [1, 2]]) == 0
    assert calc_min_path_sum(triangle=[[1], [-1, 0], [1, 0, 1]]) == 0
