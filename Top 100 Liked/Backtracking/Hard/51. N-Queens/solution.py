def solve_n_queens(n: int) -> int:
    """
    Backtracking approach.

    Time complexity: O(n^n)
    Space complexity: O(n)

    """

    def place_queens(row: int = 0):
        nonlocal cols, diags, anti_diags, solutions, board
        if row >= n:  # queens are placed
            solutions.append(["".join(row) for row in board])
            return

        for col in range(n):  # try all possible positions in current row
            # define new row
            line = ["." for _ in range(n)]
            if col not in cols and col - row not in diags and col + row not in anti_diags:
                # place queen to current field
                line[col] = "Q"
                cols.add(col)
                diags.add(col - row)
                anti_diags.add(col + row)
                board.append(line)
                # try next row
                place_queens(row + 1)

                # backtrack
                cols.remove(col)
                diags.remove(col - row)
                anti_diags.remove(col + row)
                line[col] = "."
                board.pop()
        return

    # define sets for attacked columns, diagonals, and anti-diagonals
    cols, diags, anti_diags = set(), set(), set()
    solutions, board = [], []

    place_queens()
    return solutions


if __name__ == '__main__':
    assert solve_n_queens(4) == [[".Q..", "...Q", "Q...", "..Q."], ["..Q.", "Q...", "...Q", ".Q.."]]
    assert solve_n_queens(1) == [["Q"]]
