def calc_longest_common_subseq(x: str, y: str) -> int:
    """
    Dp approach (see Readme.md)

    Time complexity: O(len(x) * len(y))
    Space complexity: O(len(x) * len(y))

    """
    dp = [[0] * (len(y) + 1) for _ in range(len(x) + 1)]
    for row in range(1, len(x) + 1):
        for col in range(1, len(y) + 1):
            diag_score = int(x[row - 1] == y[col - 1]) + dp[row - 1][col - 1]
            dp[row][col] = max(diag_score, dp[row - 1][col], dp[row][col - 1])

    return dp[-1][-1]


if __name__ == '__main__':
    actual, expected = calc_longest_common_subseq("abcde", "ace"), 3
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = calc_longest_common_subseq("abc", "abc"), 3
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = calc_longest_common_subseq("abc", "def"), 0
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = calc_longest_common_subseq("a", "aaaaa"), 1
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = calc_longest_common_subseq("b", "aaaaa"), 0
    assert actual == expected, f"expected: {expected}, actual: {actual}"
