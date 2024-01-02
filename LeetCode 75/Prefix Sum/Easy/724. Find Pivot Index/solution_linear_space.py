from typing import List


def find_pivot_element(xs: List[int]) -> int:
    """
    Define a list with backward cum sum (first pass). Then, iterate forward and compare current cum sum with
    the corresponding element in backward cum sums.


    Time complexity: O(n)
    Space complexity: O(n)

    """
    cum_sum = 0
    backward = [0] * len(xs)
    for i in range(len(xs) - 1, 0, -1):  # backward pass
        cum_sum += xs[i]
        backward[i - 1] = cum_sum

    cum_sum = 0
    for i in range(len(xs)):  # forward pass
        if cum_sum == backward[i]:
            return i
        cum_sum += xs[i]

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
