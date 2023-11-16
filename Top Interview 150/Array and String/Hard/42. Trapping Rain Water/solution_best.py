from typing import List


def calc_trap_volume(height: List[int]) -> int:
    """
    Two pointers approach.
    We don't have to keep lists with max_left and max_right values. We could calculate it on-the-fly.
    We'll calculate max_left and max_right on each step, and move towards bigger wall.

    Time complexity: O(n)
    Space complexity: O(1)
    """
    if len(height) <= 2:
        return 0

    max_left, max_right = height[0], height[-1]
    left, right = 1, len(height)-2
    total_volume = 0
    while left <= right:
        if max_left <= max_right:
            max_left = max(max_left, height[left])
            total_volume += max(0, max_left - height[left])
            left += 1
        else:
            max_right = max(max_right, height[right])
            total_volume += max(0, max_right - height[right])
            right -= 1
    return total_volume


if __name__ == '__main__':
    assert calc_trap_volume([0, 1, 0, 2, 0, 1, 0, 3, 0]) == 6
    assert calc_trap_volume([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6
    assert calc_trap_volume([4, 2, 0, 3, 2, 5]) == 9
    assert calc_trap_volume([0]) == 0
    assert calc_trap_volume([10]) == 0
    assert calc_trap_volume([0, 10]) == 0
    assert calc_trap_volume([1, 10, 1]) == 0
    assert calc_trap_volume([50, 0, 100]) == 50
    assert calc_trap_volume([50, 0, 100, 100, 40, 50]) == 60
    assert calc_trap_volume([10, 10, 10, 10]) == 0

