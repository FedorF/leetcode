from typing import List


def can_jump_to_end(nums: List[int]) -> bool:
    """
    Define "horizon" variable that shows the farthest reachable index. Update "horizon" at each step.

    Time complexity: O(N)
    Space complexity: O(1)
    """
    horizon = nums[0]
    for i in range(1, len(nums)):
        if horizon < i:
            return False
        horizon = max(horizon, i+nums[i])
    return True


if __name__ == '__main__':
    assert can_jump_to_end([2, 3, 1, 1, 4]) is True
    assert can_jump_to_end([3, 2, 1, 0, 4]) is False
    assert can_jump_to_end([0]) is True
    assert can_jump_to_end([0, 0]) is False
    assert can_jump_to_end([2, 5, 0, 0]) is True
    assert can_jump_to_end([2, 0, 0]) is True
