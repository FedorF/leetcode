def calc_levenshtein_dist(a: str, b: str) -> int:
    """
    Define DP matrix with additional row and col. Columns corresponds to a word, row to b word.
    Additional row and col corresponds to empty strs.
    At each step we'll find the min number operations needed to get to current state. It depends on three prev elements:
    left, upper, and left-up-diagonal.


    Time Complexity: O(len(a) * len(b))
    Space Complexity: O(len(a) * len(b))

    """
    dp = [0] * (len(a) + 1)
    dp = [dp[:] for i in range(len(b) + 1)]
    for row in range(len(dp)):
        for col in range(len(dp[0])):
            if row == 0:
                dp[row][col] = col
                continue

            if col == 0:
                dp[row][col] = row
                continue
            if a[col - 1] == b[row - 1]:
                replace_cost = 0
            else:
                replace_cost = 1

            dp[row][col] = min(
                dp[row - 1][col - 1] + replace_cost,  # replace cost
                dp[row - 1][col] + 1,  # delete cost
                dp[row][col - 1] + 1  # insert cost
            )
    return dp[-1][-1]


if __name__ == '__main__':
    assert calc_levenshtein_dist("intention", "execution") == 5
    assert calc_levenshtein_dist("horse", "ros") == 3
    assert calc_levenshtein_dist("horse", "") == 5
    assert calc_levenshtein_dist("", "") == 0
    assert calc_levenshtein_dist("horse", "horse") == 0
    assert calc_levenshtein_dist("a", "a") == 0
