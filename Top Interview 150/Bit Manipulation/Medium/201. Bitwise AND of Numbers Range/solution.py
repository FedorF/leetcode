def calc_bitwise_and_in_range(left: int, right: int) -> int:
    """
    Brian Kernighan's Algorithm


    Time complexity: O(log(n))
    Space complexity: O(1)

    """
    while right > left:
        right &= (right - 1)

    return right


if __name__ == '__main__':
    actual, expected = calc_bitwise_and_in_range(left=5, right=27), 4
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = calc_bitwise_and_in_range(left=0, right=0), 0
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = calc_bitwise_and_in_range(left=0, right=2147483647), 0
    assert actual == expected, f"expected: {expected}, actual: {actual}"
