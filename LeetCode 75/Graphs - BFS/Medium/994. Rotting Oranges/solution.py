from collections import deque
from typing import List


def count_steps_to_rotting(grid: List[List[str]]) -> bool:
    """
    BFS Graph approach.


    Time complexity: O(m*n)
    Space complexity: O(m*n)

    """
    n_rows, n_cols = len(grid), len(grid[0])
    fresh_cnt, rotten_cnt = 0, 0
    rotten = deque()
    seen = {}

    # initiate rotten queue
    # store node coordinates and number of steps to reach this node from the nearest "rotten" one
    for row in range(n_rows):
        for col in range(n_cols):
            if grid[row][col] == 2:
                rotten_cnt += 1
                rotten.append((row, col, 0))
                seen[(row, col)] = 0

            if grid[row][col] == 1:
                fresh_cnt += 1

    if fresh_cnt == 0:
        return 0

    if rotten_cnt == 0:
        return -1

    # start BFS
    while rotten:
        # consider "rotten" node
        row, col, step = rotten.popleft()

        # consider all adjacent nodes
        for i, j in [(row, col - 1), (row, col + 1), (row - 1, col), (row + 1, col)]:
            # if neighboring node is "fresh" and not seen, add it to queue
            if (0 <= i < n_rows) and (0 <= j < n_cols) and (grid[i][j] == 1) and ((i, j) not in seen):
                rotten.append((i, j, step + 1))
                seen[(i, j,)] = step + 1

    # there are fresh nodes left
    if len(seen) != rotten_cnt + fresh_cnt:
        return -1

    # return the furthest "fresh" node
    return max(seen.values())


if __name__ == '__main__':
    actual, expected = count_steps_to_rotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]]), 4
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = count_steps_to_rotting([[2, 1, 1], [0, 1, 1], [1, 0, 1]]), -1
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = count_steps_to_rotting([[0, 2]]), 0
    assert actual == expected, f"expected: {expected}, actual: {actual}"
