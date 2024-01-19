from typing import List


def contains_duplicate(xs: List[int]) -> bool:
    """

    Time complexity: O(n)
    Space complexity: O(n)

    """
    return len(xs) != len(set(xs))


if __name__ == '__main__':
    actual, expected = contains_duplicate([1, 2, 3, 1]), True
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = contains_duplicate([1, 2, 3, 4]), False
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = contains_duplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]), True
    assert actual == expected, f"expected: {expected}, actual: {actual}"
