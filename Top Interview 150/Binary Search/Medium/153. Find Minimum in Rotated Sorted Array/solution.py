from typing import List


def min_rotated_list(xs: List[int]) -> int:
    """
    Find pivot element. On each iteration check part, where max and min elements are adjacent.
    For example, in the list [4, 5, 6 |7| 8, 0, 1, 2] the left side is sorted, so the pivot element is on the left side.

    Time complexity: O(log(n))
    Space complexity: O(1)

    """
    if xs[0] <= xs[-1]:  # list is not rotated
        return xs[0]

    left, right = 0, len(xs) - 1
    while left < right:
        mid = left + (right - left) // 2
        if xs[right] < xs[mid]:  # pivot is in the right part
            left = mid + 1
        else:  # pivot is in the left part
            right = mid

    return xs[left]


if __name__ == '__main__':
    actual, expected = min_rotated_list(xs=[3, 1, 2]), 1
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = min_rotated_list(xs=[3, 4, 5, 1, 2]), 1
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = min_rotated_list(xs=[4, 5, 6, 7, 0, 1, 2]), 0
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = min_rotated_list(xs=[11, 13, 15, 17]), 11
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = min_rotated_list(xs=[11]), 11
    assert actual == expected, f"expected: {expected}, actual: {actual}"
