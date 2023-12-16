from typing import List


def calc_max_non_zero_sq(xs: List[List[str]]) -> int:
    """
    Starting from lower right corner, let's check what's max positive square we can achieve, if current element is an
    "upper right corner" of new square.


    Time complexity: O(n^2)
    Space complexity: O(1), due to in-place computation.

    """
    max_sq = 0
    for i in range(len(xs) - 1, -1, -1):
        for j in range(len(xs[0]) - 1, -1, -1):
            if xs[i][j] == "0":  # we can't make a positive square starting with cur element.
                xs[i][j] = 0
                continue

            if (i == len(xs) - 1) or (j == len(xs[0]) - 1):  # we are on the right/down edge
                xs[i][j] = int(xs[i][j])

            else:  # we can make at least 1 sq. square
                xs[i][j] = 1 + min(
                    int(xs[i + 1][j]),  # check right
                    int(xs[i][j + 1]),  # check down
                    int(xs[i + 1][j + 1])  # check diagonal
                )
            max_sq = max(max_sq, xs[i][j] ** 2)  # update max possible positive square

    return max_sq


if __name__ == '__main__':
    m = [["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], ["1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"]]
    assert calc_max_non_zero_sq(m) == 4
    assert calc_max_non_zero_sq([["0", "1"], ["1", "0"]]) == 1
    assert calc_max_non_zero_sq([["0"]]) == 0
    assert calc_max_non_zero_sq([["1"]]) == 1
    assert calc_max_non_zero_sq([["1", "1"]]) == 1
