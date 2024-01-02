from typing import List


def find_pivot_element(xs: List[int]) -> int:
    """
    Calculate total sum of elements (backward cum-sum). Then, iterate forward, calculate forward cum-sum, subtract
    current element from the backward cum-sum, and compare them.


    Time complexity: O(n)
    Space complexity: O(1)

    """
    backward = sum(xs)
    forward = 0
    for i in range(len(xs)):
        backward -= xs[i]
        if backward == forward:
            return i

        forward += xs[i]

    return -1


if __name__ == '__main__':
    actual, expected = find_pivot_element([1, 7, 3, 6, 5, 6]), 3
    assert actual == expected, f"actual: {actual}, expected: {expected}"

    actual, expected = find_pivot_element([1, 2, 3]), -1
    assert actual == expected, f"actual: {actual}, expected: {expected}"

    actual, expected = find_pivot_element([2, 1, -1]), 0
    assert actual == expected, f"actual: {actual}, expected: {expected}"

    actual, expected = find_pivot_element([100]), 0
    assert actual == expected, f"actual: {actual}, expected: {expected}"

    actual, expected = find_pivot_element([0]), 0
    assert actual == expected, f"actual: {actual}, expected: {expected}"
