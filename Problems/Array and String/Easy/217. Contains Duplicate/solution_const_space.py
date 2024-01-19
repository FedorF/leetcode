from typing import List


def contains_duplicate(xs: List[int]) -> bool:
    """

    Time complexity: O(n * log(n))
    Space complexity: O(1)

    """
    if len(xs) == 1:
        return False

    xs = sorted(xs)
    for i in range(1, len(xs)):
        if xs[i] == xs[i - 1]:
            return True

    return False


if __name__ == '__main__':
    actual, expected = contains_duplicate([1, 2, 3, 1]), True
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = contains_duplicate([1, 2, 3, 4]), False
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = contains_duplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]), True
    assert actual == expected, f"expected: {expected}, actual: {actual}"
