from typing import List


def find_max_volume(height: List[int]) -> int:
    """
    Calculate volume at each step and update max_volume if needed. Move pointer toward greater wall.

    Time complexity: O(N)
    Space complexity: O(1)
    """
    max_volume = 0
    left, right = 0, len(height)-1
    while left < right:
        volume = (right - left) * min(height[left], height[right])  # calculate current volume
        max_volume = max(volume, max_volume)
        if height[left] < height[right]:  # move toward the greater wall
            left += 1
        else:
            right -= 1
    return max_volume


if __name__ == '__main__':
    assert find_max_volume(height=[1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
    assert find_max_volume(height=[1, 1]) == 1
    assert find_max_volume(height=[1, 0]) == 0
