from typing import List


def calc_trap_volume(height: List[int]) -> int:
    """
    Define and fill lists with max left and max right volumes.

    Time complexity: O(n)
    Space complexity: O(n)
    """
    max_left = [0]
    cur_max_left = 0
    for i in range(1, len(height)):
        cur_max_left = max(cur_max_left, height[i - 1])
        max_left.append(cur_max_left)

    max_right = [0]
    cur_max_right = 0
    for i in range(len(height) - 2, -1, -1):
        cur_max_right = max(cur_max_right, height[i + 1])
        max_right.append(cur_max_right)

    total_volume = 0
    for i in range(len(height)):
        volume = min(max_left[i], max_right[-i - 1]) - height[i]
        total_volume += max(0, volume)
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
