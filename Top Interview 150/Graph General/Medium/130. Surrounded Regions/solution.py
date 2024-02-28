from typing import List


def flip_surrounded_regions(board: List[List[str]]):
    """
    DFS Graph approach.
    Instead of finding surrounded regions, let's find "un-surrounded", that adjacent with "O" on the border.


    Time complexity: O(n*m)
    Space complexity: O(1)

    """
    n_rows, n_cols = len(board), len(board[0])
    if n_rows < 3 or n_cols < 3:
        return

    def dfs(row: int, col: int):
        """
        Flips "O" -> "*"
        """
        for x, y in [(row, col - 1), (row, col + 1), (row - 1, col), (row + 1, col)]:
            if (0 < x < n_rows - 1) and (0 < y < n_cols - 1) and (board[x][y] == "O"):
                board[x][y] = "*"
                dfs(x, y)

    for row in range(n_rows):
        for col in range(n_cols):
            # consider only borders
            if (row in [0, n_rows - 1]) or (col in [0, n_cols - 1]):
                # and only "O"-s
                if board[row][col] == "O":
                    # find all internal cells adjacent with current border "O"
                    dfs(row, col)

    # run through all internal elements, and make a flip: "O" -> "X";  "*" -> "O"
    for row in range(1, n_rows - 1):
        for col in range(1, n_cols - 1):
            if board[row][col] == "O":
                board[row][col] = "X"

            if board[row][col] == "*":
                board[row][col] = "O"


if __name__ == '__main__':
    grid = [
        ["O", "O", "O"],
        ["O", "O", "O"],
        ["O", "O", "O"]
    ]
    expected = [
        ["O", "O", "O"],
        ["O", "O", "O"],
        ["O", "O", "O"]
    ]
    flip_surrounded_regions(grid)
    assert grid == expected, f"expected: {expected}, actual: {grid}"

    grid = [
        ["X", "X", "X"],
        ["X", "O", "X"],
        ["X", "X", "X"]
    ]
    expected = [
        ["X", "X", "X"],
        ["X", "X", "X"],
        ["X", "X", "X"]
    ]
    flip_surrounded_regions(grid)
    assert grid == expected, f"expected: {expected}, actual: {grid}"

    grid = [
        ["X", "X", "X", "X"],
        ["X", "O", "O", "X"],
        ["X", "X", "O", "X"],
        ["X", "O", "X", "X"]
    ]
    expected = [
        ["X", "X", "X", "X"],
        ["X", "X", "X", "X"],
        ["X", "X", "X", "X"],
        ["X", "O", "X", "X"]
    ]
    flip_surrounded_regions(grid)
    assert grid == expected, f"expected: {expected}, actual: {grid}"

    grid = [
        ["X"]
    ]
    expected = [
        ["X"]
    ]
    flip_surrounded_regions(grid)
    assert grid == expected, f"expected: {expected}, actual: {grid}"
