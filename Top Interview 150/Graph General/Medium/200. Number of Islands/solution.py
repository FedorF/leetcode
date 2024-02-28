from typing import List


def count_islands(grid: List[List[str]]) -> int:
    """
    DFS Graph approach.


    Time complexity: O(m*n)
    Space complexity: O(1)

    """
    n_rows, n_cols = len(grid), len(grid[0])

    def dfs(row, col):
        for x, y in [(row, col - 1), (row, col + 1), (row - 1, col), (row + 1, col)]:
            if (0 <= x < n_rows) and (0 <= y < n_cols) and (grid[x][y] == "1"):
                grid[x][y] = "*"
                dfs(x, y)

    cnt = 0
    for row in range(n_rows):
        for col in range(n_cols):
            if grid[row][col] == "1":
                grid[row][col] = "*"
                cnt += 1
                dfs(row, col)

    return cnt


if __name__ == '__main__':
    grid = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]
    actual, expected = count_islands(grid), 1
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]
    actual, expected = count_islands(grid), 3
    assert actual == expected, f"expected: {expected}, actual: {actual}"
