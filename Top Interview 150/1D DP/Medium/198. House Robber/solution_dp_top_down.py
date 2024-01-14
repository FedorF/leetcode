from typing import List


def calc_max_reward(nums: List[int]) -> int:
    """
    Top-down DP approach. Changes input list in-place.


    Time complexity: O(n)
    Space complexity: O(1)

    """
    if len(nums) < 3:
        return max(nums)

    nums[2] += nums[0]
    for i in range(3, len(nums)):
        nums[i] += max(nums[i - 2], nums[i - 3])

    return max(nums[-1], nums[-2])


if __name__ == '__main__':
    assert calc_max_reward([1, 2, 3, 1]) == 4
    assert calc_max_reward([2, 7, 9, 3, 1]) == 12
    assert calc_max_reward([100]) == 100
    assert calc_max_reward([0, 0, 0]) == 0
    assert calc_max_reward([10, 50]) == 50
    assert calc_max_reward([100, 1, 2, 50]) == 150
    assert calc_max_reward([100, 1, 3]) == 103
    assert calc_max_reward([10, 150, 15]) == 150
