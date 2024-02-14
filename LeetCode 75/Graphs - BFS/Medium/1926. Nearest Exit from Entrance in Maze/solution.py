from collections import deque
from typing import List


def calc_min_steps_to_exit(maze: List[List[str]], entrance: List[int]) -> int:
    """
    BFS Graph approach.

    Time complexity: O(m*n) ???
    Space complexity: O(m*n)

    """
    n_rows, n_cols = len(maze), len(maze[0])
    min_steps = n_rows * n_cols
    seen = {(entrance[0], entrance[1])}

    # keep coordinates and current number of steps in queue
    queue = deque([((entrance[0], entrance[1]), 0)])
    while queue:
        # consider new node
        node, steps = queue.popleft()
        row, col = node
        if row in [0, n_rows - 1] or col in [0, n_cols - 1]:  # node is on the edge of maze
            if [row, col] != entrance:  # ignore the case, when it's an entrance
                min_steps = min(min_steps, steps)
                continue

        # consider adjacent nodes
        for adj_row, adj_col in [(row, col - 1), (row, col + 1), (row - 1, col), (row + 1, col)]:
            if (adj_row, adj_col) not in seen:
                if (0 <= adj_row < n_rows) and (0 <= adj_col < n_cols) and maze[adj_row][adj_col] == ".":
                    queue.append(((adj_row, adj_col), steps + 1))
                    # add node to "seen" here, in order to avoid duplicates in queue and avoid "TLE"
                    seen.add((adj_row, adj_col))

    if min_steps == n_rows * n_cols:
        return -1

    return min_steps


if __name__ == '__main__':
    maze = [["+", "+", ".", "+"],
            [".", ".", ".", "+"],
            ["+", "+", "+", "."]]
    actual, expected = calc_min_steps_to_exit(maze, [1, 2]), 1
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    maze = [["+", "+", "+"],
            [".", ".", "."],
            ["+", "+", "+"]]
    actual, expected = calc_min_steps_to_exit(maze, [1, 0]), 2
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = calc_min_steps_to_exit(maze=[[".", "+"]], entrance=[0, 0]), -1
    assert actual == expected, f"expected: {expected}, actual: {actual}"
