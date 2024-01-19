from typing import List


def is_valid_sudoku(board: List[List[str]]) -> bool:
    """
    Define dictionaries to keep track on elements that are already seen in row, column and box.
    Traverse through all elements and check if this element has been already seen in corresponding dictionaries.

    Time complexity: O(n^2)
    Space complexity: O(n^2)

    """
    rows, cols, boxes = {}, {}, {}
    for row in range(len(board)):
        if row not in rows:
            rows[row] = set()

        for col in range(len(board)):
            if col not in cols:
                cols[col] = set()

            box = (row // 3, col // 3)
            if box not in boxes:
                boxes[box] = set()

            element = board[row][col]
            if element.isalnum():
                if (element in rows[row]) or (element in cols[col]) or (element in boxes[box]):
                    return False

                rows[row].add(element)
                cols[col].add(element)
                boxes[box].add(element)

    return True


if __name__ == '__main__':
    board = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
             ["6", ".", ".", "1", "9", "5", ".", ".", "."],
             [".", "9", "8", ".", ".", ".", ".", "6", "."],
             ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
             ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
             ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
             [".", "6", ".", ".", ".", ".", "2", "8", "."],
             [".", ".", ".", "4", "1", "9", ".", ".", "5"],
             [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    assert is_valid_sudoku(board) is True

    board = [["8", "3", ".", ".", "7", ".", ".", ".", "."],
             ["6", ".", ".", "1", "9", "5", ".", ".", "."],
             [".", "9", "8", ".", ".", ".", ".", "6", "."],
             ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
             ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
             ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
             [".", "6", ".", ".", ".", ".", "2", "8", "."],
             [".", ".", ".", "4", "1", "9", ".", ".", "5"],
             [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    assert is_valid_sudoku(board) is False
