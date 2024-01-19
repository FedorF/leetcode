from typing import List


def reverse_string(s: List[str]) -> List[str]:
    """

    Time complexity: O(n)
    Space complexity: O(1)

    """
    for i in range(len(s) // 2):
        s[i], s[len(s) - i - 1] = s[len(s) - i - 1], s[i]


if __name__ == '__main__':
    actual, expected = ["h", "e", "l", "l", "o"], ["o", "l", "l", "e", "h"]
    reverse_string(actual)
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = ["H", "a", "n", "n", "a", "h"], ["h", "a", "n", "n", "a", "H"]
    reverse_string(actual)
    assert actual == expected, f"expected: {expected}, actual: {actual}"
