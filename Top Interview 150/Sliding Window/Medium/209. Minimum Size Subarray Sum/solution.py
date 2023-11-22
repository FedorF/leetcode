from typing import List


def calc_min_size_sublist(target: int, nums: List[int]) -> int:
    """
    Sliding window approach. Keep track on two pointers: left and right border of sub-array.
    This is a linear time complexity, because both pointers linearly iterates across the list, so complexity would be
    O(2*n) ~ O(n)

    Time complexity: O(n)
    Space complexity: O(1)
    """
    cur_sum = left = 0
    min_size = len(nums) + 1
    for right in range(len(nums)):
        if nums[right] >= target:
            return 1

        cur_sum += nums[right]
        while cur_sum >= target:  # met condition
            min_size = min(min_size, right - left + 1)  # update the result
            cur_sum -= nums[left]  # update current sub-list sum
            left += 1  # move left pointer

    return min_size if min_size <= len(nums) else 0


if __name__ == '__main__':
    assert calc_min_size_sublist(target=300, nums=[1, 1, 1]) == 0
    assert calc_min_size_sublist(target=3, nums=[1, 1, 1]) == 3
    assert calc_min_size_sublist(target=7, nums=[2, 3, 1, 2, 4, 3]) == 2
    assert calc_min_size_sublist(target=4, nums=[1, 4, 4]) == 1
    assert calc_min_size_sublist(target=11, nums=[1, 1, 1, 1, 1, 1, 1, 1]) == 0
    assert calc_min_size_sublist(target=10, nums=[10]) == 1
    assert calc_min_size_sublist(target=10, nums=[1]) == 0
    assert calc_min_size_sublist(target=213, nums=[12, 28, 83, 4, 25, 26, 25, 2, 25, 25, 25, 12]) == 8
