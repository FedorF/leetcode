from typing import List


def check_el_in_matrix(xs: List[List[int]], target: int) -> bool:
    """
    1. Find candidate row.
    2. Check if element is in candidate row.


    Time complexity: O(log(m) + log(n) = log(m*n))
    Space complexity: O(1)

    """
    n_rows, n_cols = len(xs), len(xs[0])

    # find candidate row
    found_row = None
    left, right = 0, n_rows - 1
    while left <= right and found_row is None:
        mid = left + (right - left) // 2
        if xs[mid][0] <= target <= xs[mid][-1]:
            found_row = mid

        elif target < xs[mid][0]:
            right = mid - 1

        else:
            left = mid + 1

    if found_row is None:
        return False

    # check candidate row
    left, right = 0, n_cols - 1
    while left <= right:
        mid = left + (right - left) // 2
        if target == xs[found_row][mid]:
            return True
        elif target < xs[found_row][mid]:
            right = mid - 1
        else:
            left = mid + 1

    return False


if __name__ == '__main__':
    actual, expected = check_el_in_matrix(xs=[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], target=3), True
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = check_el_in_matrix(xs=[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], target=13), False
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = check_el_in_matrix(xs=[[1], [2]], target=10), False
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = check_el_in_matrix(xs=[[1], [2]], target=1), True
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = check_el_in_matrix(xs=[[1, 2]], target=1), True
    assert actual == expected, f"expected: {expected}, actual: {actual}"
