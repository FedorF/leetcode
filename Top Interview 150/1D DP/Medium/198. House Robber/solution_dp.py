from typing import List


def calc_max_reward(nums: List[int]) -> int:
    """
    DP approach. Changes input list in-place. (See details in Readme.md).
    Use last two houses as base cases.
    Start at last 3 house and calculate maximum reward at each step.
    At the end compare rewards gotten from 1 and 2 positions.

    Time complexity: O(n)
    Space complexity: O(1)
    """
    nums.append(0)  # add fake house with zero reward in order not to raise error in loop.
    i = len(nums) - 4
    while i >= 0:
        nums[i] += max(nums[i + 2], nums[i + 3])
        i -= 1
    return max(nums[:2])


if __name__ == '__main__':
    assert calc_max_reward([1, 2, 3, 1]) == 4
    assert calc_max_reward([2, 7, 9, 3, 1]) == 12
    assert calc_max_reward([100]) == 100
    assert calc_max_reward([0, 0, 0]) == 0
    assert calc_max_reward([10, 50]) == 50
    assert calc_max_reward([100, 1, 2, 50]) == 150
    assert calc_max_reward([100, 1, 3]) == 103
    assert calc_max_reward([10, 150, 15]) == 150
