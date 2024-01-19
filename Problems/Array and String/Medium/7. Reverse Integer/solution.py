def contains_duplicate(x: int) -> int:
    """

    Time complexity: O(n)
    Space complexity: O(n)

    """
    _min, _max = str(2 ** 31), str(2 ** 31 - 1)
    x = str(x)
    if x[0] == "-":
        x = x[-1:0:-1]
        if len(x) > len(_min):
            return 0
        elif len(x) == len(_min) and x > _min:
            return 0
        else:
            return -int(x)
    else:
        x = x[::-1]
        if len(x) > len(_max):
            return 0
        elif len(x) == len(_max) and x > _max:
            return 0
        else:
            return int(x)


if __name__ == '__main__':
    actual, expected = contains_duplicate(123), 321
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = contains_duplicate(-123), -321
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = contains_duplicate(120), 21
    assert actual == expected, f"expected: {expected}, actual: {actual}"
