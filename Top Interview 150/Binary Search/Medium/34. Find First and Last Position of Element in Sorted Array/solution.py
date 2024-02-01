from typing import List


def find_target_interval(xs: List[int], target: int) -> List[int]:
    """
    Apply binary search two times:
    1. To find left-most insertion position
    2. To find right-most insertion position


    Time complexity: O(log(n) + log(n) ~ log(n))
    Space complexity: O(1)

    """
    left, right = 0, len(xs)
    while left < right:  # find left-most insertion position
        mid = left + (right - left) // 2
        if target <= xs[mid]:
            right = mid
        else:
            left = mid + 1

    # if left_border element is equal to target, start right-border search
    if left < len(xs) and xs[left] == target:
        left_border = left
        right = len(xs)
        while left < right:
            mid = left + (right - left) // 2
            if target < xs[mid]:
                right = mid
            else:
                left = mid + 1

        return [left_border, left - 1]

    return [-1, -1]


if __name__ == '__main__':
    actual, expected = find_target_interval(xs=[2, 2], target=2), [0, 1]
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = find_target_interval(xs=[2, 2], target=3), [-1, -1]
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = find_target_interval(xs=[], target=0), [-1, -1]
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = find_target_interval(xs=[1, 2], target=0), [-1, -1]
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = find_target_interval(xs=[1, 2], target=1), [0, 0]
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = find_target_interval(xs=[1], target=100), [-1, -1]
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = find_target_interval(xs=[1], target=1), [0, 0]
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = find_target_interval([5, 7, 7, 8, 8, 10], target=8), [3, 4]
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = find_target_interval(xs=[5, 7, 7, 8, 8, 10], target=6), [-1, -1]
    assert actual == expected, f"expected: {expected}, actual: {actual}"
