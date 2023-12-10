from typing import List


def calc_max_reward(nums: List[int]) -> int:
    """
    DFS + Memoization approach. See tree in Readme.md.
    We'll start either at 1 or 2 position.
    And we have choice to rob i+2 house or i+3.
    Cache already calculated steps.
    At the end compare rewards gotten from 1 and 2 positions.

    Time complexity: O(n)
    Space complexity: O(n)
    """
    if len(nums) == 1:
        return nums[0]

    def dfs(cur_ind: int) -> int:
        if cur_ind > len(nums) - 1:
            return 0

        if (cur_ind == len(nums) - 1) or (cur_ind == len(nums) - 2):
            return nums[cur_ind]

        if cur_ind in cache:
            return cache[cur_ind]

        cache[cur_ind] = nums[cur_ind] + max(dfs(cur_ind + 2), dfs(cur_ind + 3))
        return cache[cur_ind]

    cache = {}
    return max(dfs(0), dfs(1))


if __name__ == '__main__':
    assert calc_max_reward([1, 2, 3, 1]) == 4
    assert calc_max_reward([2, 7, 9, 3, 1]) == 12
    assert calc_max_reward([100]) == 100
    assert calc_max_reward([0, 0, 0]) == 0
    assert calc_max_reward([10, 50]) == 50
    assert calc_max_reward([100, 1, 2, 50]) == 150
    assert calc_max_reward([100, 1, 3]) == 103
    assert calc_max_reward([10, 150, 15]) == 150
