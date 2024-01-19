from typing import List


def reverse_string(s: List[str]) -> List[str]:
    """

    Time complexity: O(n)
    Space complexity: O(1)

    """
    l, r = 0, len(s) - 1
    while l <= r:
        s[l], s[r] = s[r], s[l]
        l += 1
        r -= 1


if __name__ == '__main__':
    actual, expected = ["h", "e", "l", "l", "o"], ["o", "l", "l", "e", "h"]
    reverse_string(actual)
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = ["H", "a", "n", "n", "a", "h"], ["h", "a", "n", "n", "a", "H"]
    reverse_string(actual)
    assert actual == expected, f"expected: {expected}, actual: {actual}"
