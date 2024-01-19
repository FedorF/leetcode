def calc_num_steps_to_reduce_to_zero(x: int) -> int:
    """


    Time complexity: O(n)
    Space complexity: O(1)

    """
    num_steps = 0
    while x > 0:
        if x % 2 == 0:
            x //= 2
        else:
            x -= 1
        num_steps += 1

    return num_steps


if __name__ == '__main__':
    actual, expected = calc_num_steps_to_reduce_to_zero(14), 6
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = calc_num_steps_to_reduce_to_zero(8), 4
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = calc_num_steps_to_reduce_to_zero(123), 12
    assert actual == expected, f"expected: {expected}, actual: {actual}"
