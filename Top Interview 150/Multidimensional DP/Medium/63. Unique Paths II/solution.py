from typing import List


def count_unique_paths(grid: List[List[int]]) -> int:
    """
    DP (bottom-up) approach. Start with first element (base case) and continue calculations of "how many ways are there
    to get to current square".
    We'll fill every square with number of ways to get there. If it's an obstacle, set its value to 0.

    Time complexity: O(n^2)
    Space complexity: O(1), due to in-place calculations

    """
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if row == 0 and col == 0:  # base case
                if grid[row][col] == 1:
                    return 0
                else:
                    grid[row][col] = 1
                    continue

            if grid[row][col] == 1:  # found obstacle
                grid[row][col] = 0
                continue

            if row == 0:
                grid[row][col] += grid[row][col - 1]
                continue

            if col == 0:
                grid[row][col] += grid[row - 1][col]
                continue

            grid[row][col] += grid[row][col - 1] + grid[row - 1][col]

    return grid[-1][-1]


if __name__ == '__main__':
    assert count_unique_paths([[0, 0, 0], [0, 1, 0], [0, 0, 0]]) == 2
    assert count_unique_paths([[0, 1], [0, 0]]) == 1
    assert count_unique_paths([[1]]) == 0
    assert count_unique_paths([[0]]) == 1
