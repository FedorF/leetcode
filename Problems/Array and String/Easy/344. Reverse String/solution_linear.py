from typing import List


def reverse_string(s: List[str]) -> List[str]:
    """

    Time complexity: O(n)
    Space complexity: O(n)

    """
    return s[::-1]


if __name__ == '__main__':
    actual, expected = reverse_string(["h", "e", "l", "l", "o"]), ["o", "l", "l", "e", "h"]
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = reverse_string(["H", "a", "n", "n", "a", "h"]), ["h", "a", "n", "n", "a", "H"]
    assert actual == expected, f"expected: {expected}, actual: {actual}"
