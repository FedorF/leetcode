def calc_tiling_variations(n: int) -> int:
    """
    See induction formula in Readme.md.


    Time complexity: O(n)
    Space complexity: O(n)

    """
    mod = 1e9 + 7
    dp = [1, 1, 2, 5]
    if n <= 3:
        return dp[n]

    for i in range(4, n + 1):
        x = 2 * dp[i - 1] + dp[i - 3]
        dp.append(int(x % mod))

    return dp[-1]


if __name__ == '__main__':
    actual, expected = calc_tiling_variations(5), 24
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = calc_tiling_variations(4), 11
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = calc_tiling_variations(3), 5
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = calc_tiling_variations(1), 1
    assert actual == expected, f"expected: {expected}, actual: {actual}"
