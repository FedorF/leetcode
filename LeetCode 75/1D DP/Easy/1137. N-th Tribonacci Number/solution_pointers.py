def find_tribonacci_number(n: int) -> int:
    """
    We don't need a list to keep all numbers, we just can use three pointers.

    Time complexity: O(n)
    Space complexity: O(1)

    """
    if n == 0:
        return 0

    if n == 1 or n == 2:
        return 1

    first, second, third = 0, 1, 1
    for i in range(n - 2):
        first, second, third = second, third, first + second + third

    return third


if __name__ == '__main__':
    actual, expected = find_tribonacci_number(0), 0
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = find_tribonacci_number(4), 4
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = find_tribonacci_number(25), 1389537
    assert actual == expected, f"expected: {expected}, actual: {actual}"
