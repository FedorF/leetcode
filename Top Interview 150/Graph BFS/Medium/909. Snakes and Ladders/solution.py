from collections import deque
from typing import List


def calc_min_steps(board: List[List[int]]) -> int:
    """
    BFS approach.


    Time complexity: O(n^2)
    Space complexity: O(n^2)

    """
    n = len(board)
    graph = {}  # maps i -> board cell's value
    i, col, rightwise = 1, 0, True
    for row in range(n - 1, -1, -1):  # fill graph using Boustrophedon order
        if rightwise:
            while col < n:
                graph[i] = board[row][col]
                i += 1
                col += 1
            rightwise = False
            col -= 1
        else:
            while col >= 0:
                graph[i] = board[row][col]
                i += 1
                col -= 1
            rightwise = True
            col += 1

    queue = deque([(1, 0)])
    seen = {1}
    while queue:
        i, steps = queue.popleft()
        for dice in range(1, 7):
            next_i = i + dice
            if graph[next_i] != -1:  # found shortcut
                next_i = graph[next_i]

            if next_i == n ** 2:  # reached last cell
                return steps + 1

            if next_i not in seen:
                seen.add(next_i)
                queue.append((next_i, steps + 1))

    return -1


if __name__ == '__main__':
    board = [
        [-1, -1, -1, -1, 48, 5, -1],
        [12, 29, 13, 9, -1, 2, 32],
        [-1, -1, 21, 7, -1, 12, 49],
        [42, 37, 21, 40, -1, 22, 12],
        [42, -1, 2, -1, -1, -1, 6],
        [39, -1, 35, -1, -1, 39, -1],
        [-1, 36, -1, -1, -1, -1, 5],
    ]
    actual, expected = calc_min_steps(board), 3
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    board = [
        [-1, -1, 30, 14, 15, -1],
        [23, 9, -1, -1, -1, 9],
        [12, 5, 7, 24, -1, 30],
        [10, -1, -1, -1, 25, 17],
        [32, -1, 28, -1, -1, 32],
        [-1, -1, 23, -1, 13, 19],
    ]
    actual, expected = calc_min_steps(board), 2
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    board = [
        [-1, 1, 2, -1],
        [2, 13, 15, -1],
        [-1, 10, -1, -1],
        [-1, 6, 2, 8],
    ]
    actual, expected = calc_min_steps(board), 2
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    board = [
        [-1, 7, -1],
        [-1, 6, 9],
        [-1, -1, 2],
    ]
    actual, expected = calc_min_steps(board), 1
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    board = [
        [-1, -1, -1],
        [-1, 9, 8],
        [-1, 8, 9],
    ]
    actual, expected = calc_min_steps(board), 1
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    board = [
        [-1, -1],
        [-1, 3],
    ]
    actual, expected = calc_min_steps(board), 1
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    board = [
        [-1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1],
        [-1, 35, -1, -1, 13, -1],
        [-1, -1, -1, -1, -1, -1],
        [-1, 15, -1, -1, -1, -1],
    ]
    actual, expected = calc_min_steps(board), 4
    assert actual == expected, f"expected: {expected}, actual: {actual}"
