def calc_pow(x: int, n: int) -> float:
    """
    Brute force solution: raises TLE!


    Time complexity: O(n)
    Space complexity: O(1)

    """
    if n == 0:
        return 1

    if x == 0 or x == 1:
        return x

    if n < 0:
        x = 1 / x
        n *= -1

    res = x
    for i in range(n - 1):
        res *= x

    return res


if __name__ == '__main__':
    actual, expected = calc_pow(x=2.00000, n=10), 1024
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = calc_pow(x=2.10000, n=3), 9.261
    assert abs(actual - expected) < 1e-5, f"expected: {expected}, actual: {actual}"

    actual, expected = calc_pow(x=2.00000, n=-2), .25
    assert actual == expected, f"expected: {expected}, actual: {actual}"
