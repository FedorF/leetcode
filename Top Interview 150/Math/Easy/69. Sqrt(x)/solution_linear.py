def calc_sqrt(n: int) -> int:
    """

    Time complexity: O(n)
    Space complexity: O(1)

    """
    root = 0
    while root * root <= n:
        root += 1

    return root - 1


if __name__ == '__main__':
    actual, expected = calc_sqrt(4), 2
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = calc_sqrt(8), 2
    assert actual == expected, f"expected: {expected}, actual: {actual}"
