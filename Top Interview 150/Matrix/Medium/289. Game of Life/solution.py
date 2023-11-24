from typing import List, Tuple


def get_neighbors(row: int, col: int, m: int, n: int) -> List[Tuple[int, int]]:
    """
    Returns cell neighbors.

    Time complexity: O(1)
    Space complexity: O(1)
    """
    neighbors = []
    if col - 1 >= 0:
        neighbors.append((row, col - 1))
    if col + 1 < n:
        neighbors.append((row, col + 1))
    if row - 1 >= 0:
        neighbors.append((row - 1, col))
    if row + 1 < m:
        neighbors.append((row + 1, col))
    if (col - 1 >= 0) and (row - 1 >= 0):
        neighbors.append((row - 1, col - 1))
    if (col - 1 >= 0) and (row + 1 < m):
        neighbors.append((row + 1, col - 1))
    if (col + 1 < n) and (row + 1 < m):
        neighbors.append((row + 1, col + 1))
    if (col + 1 < n) and (row - 1 >= 0):
        neighbors.append((row - 1, col + 1))
    return neighbors


def update_cell(cell_state: int, live_neighbors: int) -> int:
    """
    Updates cell state depending on cell's status and neighbors' status.

    Time complexity: O(1)
    Space complexity: O(1)
    """
    if cell_state > 0:
        if live_neighbors < 2 or live_neighbors > 3:
            return 0
        else:
            return 1
    else:
        if live_neighbors == 3:
            return 1
    return 0


def update_state(board: List[List[int]]):
    """
    Firstly, define m*n dictionary with cells current state; then walk through board and update cells' status.

    Time complexity: O(m*n)
    Space complexity: O(m*n)
    """
    m, n = len(board), len(board[0])
    current_state = {}
    for row in range(m):
        for col in range(n):
            current_state[(row, col)] = board[row][col]

    for row in range(m):
        for col in range(n):
            live_neighbors = 0
            for neighbor in get_neighbors(row, col, m, n):
                if neighbor in current_state:
                    live_neighbors += current_state[neighbor]
            board[row][col] = update_cell(board[row][col], live_neighbors)


if __name__ == '__main__':
    board = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
    update_state(board)
    assert board == [[0, 0, 0], [1, 0, 1], [0, 1, 1], [0, 1, 0]]

    board = [[1, 1], [1, 0]]
    update_state(board)
    assert board == [[1, 1], [1, 1]]

    board = [[1]]
    update_state(board)
    assert board == [[0]]

    board = [[0]]
    update_state(board)
    assert board == [[0]]

    board = [[1], [1]]
    update_state(board)
    assert board == [[0], [0]]

    board = [[1, 1]]
    update_state(board)
    assert board == [[0, 0]]
