from typing import List


def calc_min_path_sum(grid: List[List[int]]) -> int:
    """
    DP (bottom-up) approach. Start with first element (base case) and continue calculations for the following elements.

    Time complexity: O(n^2)
    Space complexity: O(1), due to in-place calculations

    """
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if row == 0 and col == 0:
                continue

            if row == 0:
                grid[row][col] += grid[row][col - 1]
                continue

            if col == 0:
                grid[row][col] += grid[row - 1][col]
                continue

            grid[row][col] += min(grid[row - 1][col], grid[row][col - 1])

    return grid[-1][-1]


if __name__ == '__main__':
    assert calc_min_path_sum(grid=[[1, 3, 1], [1, 5, 1], [4, 2, 1]]) == 7
    assert calc_min_path_sum(grid=[[1, 2, 3], [4, 5, 6]]) == 12
    assert calc_min_path_sum(grid=[[1], [-1]]) == 0
    assert calc_min_path_sum(grid=[[1, 2, 3]]) == 6
