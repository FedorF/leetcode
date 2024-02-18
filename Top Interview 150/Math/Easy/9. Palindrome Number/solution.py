import math


def is_palindrome(x: int) -> bool:
    """
    No converting to str approach.
    The idea is to calculate reversed number by mirroring x-th digits.
    (See Readme.md)


    Time complexity: O(n_digits)
    Space complexity: O(1)

    """
    if x < 0:
        return False

    if x == 0:
        return True

    i = int(math.log(x, 10))  # length(x) - 1
    j = 0
    x_reversed = 0
    while i >= 0:
        # find j-th digit
        digit = x // (10 ** j) % 10

        # place j-th digit onto i-th position
        x_reversed += digit * (10 ** i)
        j += 1
        i -= 1

    return x_reversed == x


if __name__ == '__main__':
    actual, expected = is_palindrome(123), False
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = is_palindrome(0), True
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = is_palindrome(1), True
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = is_palindrome(123), False
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = is_palindrome(123454321), True
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = is_palindrome(10), False
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = is_palindrome(-1), False
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = is_palindrome(1001), True
    assert actual == expected, f"expected: {expected}, actual: {actual}"
