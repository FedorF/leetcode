def calc_sqrt(n: int) -> int:
    """
    Binary search approach.

    Time complexity: O(log(n))
    Space complexity: O(1)

    """
    left, right = 0, n
    while left <= right:
        mid = left + (right - left) // 2
        if mid * mid == n:
            return mid

        if mid * mid > n:
            right = mid - 1
        else:
            left = mid + 1

    return left - 1


if __name__ == '__main__':
    actual, expected = calc_sqrt(4), 2
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = calc_sqrt(8), 2
    assert actual == expected, f"expected: {expected}, actual: {actual}"
