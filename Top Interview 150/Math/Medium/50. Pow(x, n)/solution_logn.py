def calc_pow(x: int, n: int) -> float:
    """
    Recursive solution.

    1. If power is even:
      2^10 = 2^5 * 2^5

    2. If power is odd:
      2^5 = 2 * 2^4 * 2^4


    Time complexity: O(log(n))
    Space complexity: O(log(n))

    """
    if n == 0:
        return 1

    if x == 0 or x == 1:
        return x

    def calc(power: int):
        if power == 1:
            return x

        if power in cache:
            return cache[power]

        if power % 2 == 0:
            cache[power] = calc(power // 2) * calc(power // 2)
            return cache[power]

        cache[power] = x * calc(power // 2) * calc(power // 2)
        return cache[power]

    if n < 0:
        x = 1 / x
        n *= -1

    cache = {}
    return calc(n)


if __name__ == '__main__':
    actual, expected = calc_pow(x=2.00000, n=10), 1024
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = calc_pow(x=2.10000, n=3), 9.261
    assert abs(actual - expected) < 1e-5, f"expected: {expected}, actual: {actual}"

    actual, expected = calc_pow(x=2.00000, n=-2), .25
    assert actual == expected, f"expected: {expected}, actual: {actual}"
