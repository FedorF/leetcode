def calc_queens_combs(n: int) -> int:
    """
    Backtracking approach.

    Time complexity: O(n^n)
    Space complexity: O(n)

    """
    # define sets for attacked columns, diagonals, and anti-diagonals
    cols, diag, anti_diag = set(), set(), set()

    def place_queens(row: int = 0):
        if row >= n:  # all queens were placed
            nonlocal res
            res += 1
            return

        for col in range(n):  # try all possible columns for current row
            if col not in cols and col - row not in diag and col + row not in anti_diag:
                # attack current column and diagonals
                cols.add(col)
                diag.add(col - row)
                anti_diag.add(col + row)

                place_queens(row + 1)

                # remove queen
                cols.remove(col)
                diag.remove(col - row)
                anti_diag.remove(col + row)
        return

    res = 0
    place_queens()
    return res


if __name__ == '__main__':
    assert calc_queens_combs(4) == 2
    assert calc_queens_combs(1) == 1
