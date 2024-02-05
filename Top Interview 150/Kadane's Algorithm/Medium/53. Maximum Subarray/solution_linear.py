from typing import List


def find_max_subarray_sum(xs: List[int]) -> int:
    """
    On each step check if it's better to start new subarray or continue current subarray by adding new element to
    current total sum.
    And update max_sum variable.

    Time complexity: O(n)
    Time complexity: O(1)
    """
    max_sum = cur_sum = xs[0]
    for i in range(1, len(xs)):
        cur_sum = max(cur_sum + xs[i], xs[i])  # check if it's better to start new subarray
        max_sum = max(max_sum, cur_sum)
    return max_sum


if __name__ == '__main__':
    assert find_max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
    assert find_max_subarray_sum([1]) == 1
    assert find_max_subarray_sum([5, 4, -1, 7, 8]) == 23
