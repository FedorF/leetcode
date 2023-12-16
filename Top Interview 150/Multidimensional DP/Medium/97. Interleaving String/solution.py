def is_interleave(a: str, b: str, c: str) -> bool:
    """
    Define DP matrix with additional row and col, and build a route. If we use letter from the string a, we move one
    square right. If we use letter from the string b, we move one square down.
    If we can reach lower right corner, it's an interleave.


    Time Complexity: O(len(c)^2)
    Space Complexity: O(len(c)^2)

    """
    if len(a) + len(b) != len(c):
        return False

    dp = [[False for i in range(len(a) + 1)] for j in range(len(b) + 1)]  # define dp matrix
    for row in range(len(dp)):
        for col in range(len(dp[0])):
            if row == 0 and col == 0:
                dp[0][0] = True
                continue

            if row == 0:
                dp[row][col] = (a[col - 1] == c[col - 1]) and dp[row][col - 1]
                continue

            if col == 0:
                dp[row][col] = (b[row - 1] == c[row - 1]) and dp[row - 1][col]
                continue

            if (c[col + row - 1] == a[col - 1]) and dp[row][col - 1]:
                dp[row][col] = True

            if (c[row + col - 1] == b[row - 1]) and (dp[row - 1][col]):
                dp[row][col] = True

    return dp[-1][-1]


if __name__ == '__main__':
    assert is_interleave(a="aabcc", b="dbbca", c="aadbbcbcac") is True
    assert is_interleave(a="aabcc", b="dbbca", c="aadbbbaccc") is False
    assert is_interleave(a="", b="", c="") is True
    assert is_interleave("a", "", "a") is True
    assert is_interleave(a="db", b="b", c="cbb") is False
