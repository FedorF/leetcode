def calc_unique_paths(m: int, n: int) -> int:
    """
    DP Approach (see Readme.md)


    Time complexity: O(m*n)
    Space complexity: O(m*n)

    """
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    dp[0][1] = 1
    for row in range(1, m + 1):
        for col in range(1, n + 1):
            dp[row][col] = dp[row - 1][col] + dp[row][col - 1]

    return dp[-1][-1]


if __name__ == '__main__':
    actual, expected = calc_unique_paths(m=3, n=7), 28
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = calc_unique_paths(m=3, n=2), 3
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = calc_unique_paths(1, 1), 1
    assert actual == expected, f"expected: {expected}, actual: {actual}"
