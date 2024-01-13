from typing import List


def find_peak_element_index(xs: List[int]) -> int:
    """
    Refactored version.


    Time complexity: O(log(n))
    Space complexity: O(1)

    """
    left, right = 0, len(xs) - 1
    while left <= right:
        mid = left + (right - left) // 2  # avoid overflow

        # left element is greater
        if (mid > 0) and (xs[mid] < xs[mid - 1]):
            right = mid - 1

        # right element is greater
        elif (mid < len(xs) - 1) and (xs[mid] < xs[mid + 1]):
            left = mid + 1

        else:
            return mid


if __name__ == '__main__':
    actual, expected = find_peak_element_index([1, 2, 3, 1]), 2
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = find_peak_element_index([1, 2, 1, 3, 5, 6, 4]), [1, 5]
    assert actual in expected, f"expected: {expected}, actual: {actual}"

    actual, expected = find_peak_element_index([1]), 0
    assert actual == expected, f"expected: {expected}, actual: {actual}"
