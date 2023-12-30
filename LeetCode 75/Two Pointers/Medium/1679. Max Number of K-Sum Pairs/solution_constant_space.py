from typing import List


def calc_max_num_add_operations(xs: List[int], target: int) -> int:
    """
    Sort list first, then move left-most and right-most pointers step-by-step.


    Time complexity: O(n * log(n))
    Space complexity: O(1)

    """
    xs = sorted(xs)
    res = 0
    left, right = 0, len(xs) - 1
    while left < right:
        if xs[left] + xs[right] == target:  # move both pointers
            res += 1
            left += 1
            right -= 1
        elif xs[left] + xs[right] > target:  # move right to decrease sum
            right -= 1
        else:  # move left to increase sum
            left += 1

    return res


if __name__ == '__main__':
    actual, expected = calc_max_num_add_operations(xs=[1, 2, 3, 4], target=5), 2
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = calc_max_num_add_operations(xs=[3, 1, 3, 4, 3], target=6), 1
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = calc_max_num_add_operations(xs=[3], target=3), 0
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = calc_max_num_add_operations(xs=[3], target=10), 0
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = calc_max_num_add_operations(xs=[3, 7], target=20), 0
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = calc_max_num_add_operations(xs=[3, 7], target=10), 1
    assert actual == expected, f"expected: {expected}, actual: {actual}"
