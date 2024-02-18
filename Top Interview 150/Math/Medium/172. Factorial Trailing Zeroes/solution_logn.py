def count_factorial_trailing_zeros(n: int) -> int:
    """
    de Polignac's formula: https://en.wikipedia.org/wiki/Trailing_zero


    Time complexity: O(log(n))
    Space complexity: O(1)

    """
    if n < 5:
        return 0

    cnt = 0
    while n > 0:
        cnt += n // 5
        n //= 5

    return cnt


if __name__ == '__main__':
    actual, expected = count_factorial_trailing_zeros(3), 0
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = count_factorial_trailing_zeros(5), 1
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = count_factorial_trailing_zeros(0), 0
    assert actual == expected, f"expected: {expected}, actual: {actual}"
