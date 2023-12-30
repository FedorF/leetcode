from typing import List


def find_max_area(height: List[int]) -> int:
    """
    Calculate area at each step and update max_area if needed. Move pointer toward greater wall.


    Time complexity: O(N)
    Space complexity: O(1)

    """
    max_area = 0
    left, right = 0, len(height) - 1
    while left < right:
        if height[left] <= height[right]:
            area = height[left] * (right - left)
            left += 1  # move toward the greater wall
        else:
            area = height[right] * (right - left)
            right -= 1  # move toward the greater wall

        if area > max_area:
            max_area = area

    return max_area


if __name__ == '__main__':
    assert find_max_area(height=[1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
    assert find_max_area(height=[1, 1]) == 1
    assert find_max_area(height=[1, 0]) == 0
