def calc_levenshtein_dist(a: str, b: str) -> int:
    """
    Implementation of algorithm described in https://en.wikipedia.org/wiki/Levenshtein_distance.

    Define DP matrix with additional row and col. Columns corresponds to a word, row to b word.
    Additional row and col corresponds to empty strs.
    At each step we'll find the min number operations needed to get to current state.
    It depends on three prev elements:
    - left
    - upper
    - uppper-left diagonal


    Time Complexity: O(len(a) * len(b))
    Space Complexity: O(len(a) * len(b))

    """
    dp = [[0] * (len(a) + 1) for _ in range(len(b) + 1)]
    for row in range((len(b) + 1)):
        for col in range((len(a) + 1)):
            if row == 0:
                dp[row][col] = col
                continue

            if col == 0:
                dp[row][col] = row
                continue

            dp[row][col] = min(
                dp[row - 1][col - 1] + int(a[col - 1] != b[row - 1]),  # replace cost
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
