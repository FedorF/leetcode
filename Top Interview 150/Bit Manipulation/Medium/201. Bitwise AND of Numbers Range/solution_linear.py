def calc_bitwise_and_in_range(left: int, right: int) -> int:
    """
    Brute force solution: raises "TLE"


    Time complexity: O(n)
    Space complexity: O(1)

    """
    res = left
    for x in range(left + 1, right):
        res &= x
    return res


if __name__ == '__main__':
    actual, expected = calc_bitwise_and_in_range(left=5, right=7), 4
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = calc_bitwise_and_in_range(left=0, right=0), 0
    assert actual == expected, f"expected: {expected}, actual: {actual}"
