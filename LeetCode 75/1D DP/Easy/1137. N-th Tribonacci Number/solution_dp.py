def find_tribonacci_number(n: int) -> int:
    """
    Dynamical programming approach.


    Time complexity: O(n)
    Space complexity: O(n)

    """
    dp = [0, 1, 1]
    if n < 3:
        return dp[n]

    for i in range(3, n + 1):
        dp.append(dp[i - 1] + dp[i - 2] + dp[i - 3])

    return dp[n]


if __name__ == '__main__':
    actual, expected = find_tribonacci_number(0), 0
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = find_tribonacci_number(4), 4
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = find_tribonacci_number(25), 1389537
    assert actual == expected, f"expected: {expected}, actual: {actual}"
