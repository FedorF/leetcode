from typing import List


def calc_max_reward(nums: List[int]) -> int:
    """
    Bottom-up DP approach. Same idea, but we don't change input array.
    At each step we can either rob current house and take the reward1, or we can skip current.


    Time complexity: O(n)
    Space complexity: O(1)

    """
    reward1, reward2 = 0, 0
    # [reward1, reward2, cur_house, n+1, n+2, ...]
    for cur_house in nums:
        reward1, reward2 = reward2, max(cur_house + reward1, reward2)

    return reward2


if __name__ == '__main__':
    assert calc_max_reward([1, 2, 3, 1]) == 4
    assert calc_max_reward([2, 7, 9, 3, 1]) == 12
    assert calc_max_reward([100]) == 100
    assert calc_max_reward([0, 0, 0]) == 0
    assert calc_max_reward([10, 50]) == 50
    assert calc_max_reward([100, 1, 2, 50]) == 150
    assert calc_max_reward([100, 1, 3]) == 103
    assert calc_max_reward([10, 150, 15]) == 150
