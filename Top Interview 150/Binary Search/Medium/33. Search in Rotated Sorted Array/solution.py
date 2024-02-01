from typing import List


def search_rotated_list(xs: List[int], target: int) -> int:
    """
    At each step either left part of array is sorted: [3,4,5,6 | 7,0,1,2],
    or right part is sorted: [7,0,1,2 | 4,5,6]
    So, check if target element is in sorted part first, if it's not start search in unsorted part.


    Time complexity: O(log(n))
    Space complexity: O(1)

    """
    left, right = 0, len(xs) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if target == xs[mid]:
            return mid

        # left part is sorted
        if xs[left] <= xs[mid]:
            if xs[left] <= target < xs[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:  # right part is sorted
            if xs[mid] < target <= xs[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1


if __name__ == '__main__':
    actual, expected = search_rotated_list(xs=[5, 1, 3], target=3), 2
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = search_rotated_list(xs=[4, 5, 6, 7, 0, 1, 2], target=0), 4
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = search_rotated_list(xs=[4, 5, 6, 7, 0, 1, 2], target=3), -1
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = search_rotated_list(xs=[1], target=0), -1
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = search_rotated_list(xs=[4, 5, 6, 7, 8, 1, 2, 3], target=8), 4
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = search_rotated_list(xs=[3, 1], target=1), 1
    assert actual == expected, f"expected: {expected}, actual: {actual}"
