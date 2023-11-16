from typing import List


def calc_min_jumps(nums: List[int]) -> int:
    """
    Keeps track of the farthest reachable position ("horizon") at each step and updates the number of jumps needed to
    reach that farthest position.
    Increase number of steps by 1, when reach end of current stride, and update stride variable.


    Time complexity: O(N)
    Space complexity: O(1)
    """
    if len(nums) == 1:
        return 0

    horizon = 0
    stride = 0
    steps = 1
    for i in range(len(nums)-1):
        horizon = max(horizon, i+nums[i])
        if horizon >= len(nums) - 1:
            break

        if i == stride:
            stride = horizon
            steps += 1

    return steps


if __name__ == '__main__':
    assert calc_min_jumps([2, 3, 1, 1, 4]) == 2
    assert calc_min_jumps([2, 3, 0, 1, 4]) == 2
    assert calc_min_jumps([0]) == 0
    assert calc_min_jumps([100]) == 0
    assert calc_min_jumps([1, 0]) == 1
    assert calc_min_jumps([3, 3, 1, 3, 1, 0]) == 2
