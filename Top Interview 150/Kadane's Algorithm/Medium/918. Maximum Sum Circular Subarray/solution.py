from typing import List


def find_max_circular_subarray_sum(xs: List[int]) -> int:
    """
    Check approach in Readme.md

    Time complexity: O(n)
    Space complexity: O(1)
    """
    total_sum = max_sum = cur_max = min_sum = cur_min = xs[0]
    for i in range(1, len(xs)):
        cur_max = max(xs[i], cur_max + xs[i])
        max_sum = max(max_sum, cur_max)

        cur_min = min(xs[i], cur_min + xs[i])
        min_sum = min(min_sum, cur_min)
        total_sum += xs[i]

    if max_sum > 0:
        return max(max_sum, total_sum - min_sum)

    return max_sum


if __name__ == '__main__':
    assert find_max_circular_subarray_sum([1, -2, 3, -2]) == 3
    assert find_max_circular_subarray_sum([5, -3, 5]) == 10
    assert find_max_circular_subarray_sum([-3, -2, -3]) == -2
    assert find_max_circular_subarray_sum([-100]) == -100
    assert find_max_circular_subarray_sum([0]) == 0
    assert find_max_circular_subarray_sum([0, 5, 8, -9, 9, -7, 3, -2]) == 16
