from typing import List


def find_peak_element_index(xs: List[int]) -> int:
    """
    Due to x[i] != x[i+1] and outside elements are always less than inside, it's guaranteed that applying binary search
    and moving to ascending direction we'll reach the peak element.


    Time complexity: O(log(n))
    Space complexity: O(1)

    """
    if len(xs) == 1:
        return 0

    left, right = 0, len(xs) - 1
    while left < right:
        mid = (left + right) // 2
        if (mid == 0) and (xs[mid] > xs[mid + 1]):  # reached left boundary
            return 0

        elif (mid == len(xs) - 1) and (xs[mid] > xs[mid - 1]):  # reached right boundary
            return len(xs) - 1

        elif xs[mid - 1] < xs[mid] > xs[mid + 1]:  # found peak element
            return mid

        elif xs[mid] < xs[mid + 1]:  # proceed to the right direction
            left = mid + 1
        else:  # proceed to the left direction
            right = mid


if __name__ == '__main__':
    actual, expected = find_peak_element_index([1, 2, 3, 1]), 2
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = find_peak_element_index([1, 2, 1, 3, 5, 6, 4]), [1, 5]
    assert actual in expected, f"expected: {expected}, actual: {actual}"

    actual, expected = find_peak_element_index([1]), 0
    assert actual == expected, f"expected: {expected}, actual: {actual}"
