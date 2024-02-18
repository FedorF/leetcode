def calc_sqrt(n: int) -> int:
    """
    Binary search approach.

    Time complexity: O(log(n))
    Space complexity: O(1)

    """
    root = n
    while root * root > n:
        root = (root + n / root) / 2
        root = int(root)

    return root


if __name__ == '__main__':
    actual, expected = calc_sqrt(4), 2
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = calc_sqrt(8), 2
    assert actual == expected, f"expected: {expected}, actual: {actual}"
