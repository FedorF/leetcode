from typing import List


def find_max_subarray_sum(xs: List[int]) -> int:
    """
    Brute Force approach: iterate through all possible sub-arrays, calculate it sum and update max_sum if needed.
    Raises "Time Limit Exceeded" error on Leetcode.

    Time complexity: O(n^2)
    Time complexity: O(1)
    """
    max_sum = xs[0]
    for subarray_start in range(0, len(xs)):
        cur_sum = xs[subarray_start]
        max_sum = max(cur_sum, max_sum)
        end = subarray_start + 1
        while end < len(xs):
            cur_sum += xs[end]
            max_sum = max(cur_sum, max_sum)
            end += 1
    return max_sum


if __name__ == '__main__':
    assert find_max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
    assert find_max_subarray_sum([1]) == 1
    assert find_max_subarray_sum([5, 4, -1, 7, 8]) == 23
