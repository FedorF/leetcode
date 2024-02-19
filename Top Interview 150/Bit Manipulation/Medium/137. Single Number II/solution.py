from typing import List


def find_single_number(nums: List[int]) -> int:
    """

    Space Complexity: O(n)
    Time Complexity: O(1)

    """
    # todo


if __name__ == '__main__':
    actual, expected = find_single_number([30000, 500, 100, 30000, 100, 30000, 100]), 500
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = find_single_number([2, 2, 3, 2]), 3
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = find_single_number([0, 1, 0, 1, 0, 1, 99]), 99
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = find_single_number([2, 2, 3, 2]), 3
    assert actual == expected, f"expected: {expected}, actual: {actual}"
