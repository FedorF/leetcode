from typing import List


def find_target_terms(numbers: List[int], target: int) -> List[int]:
    """
    Compare difference between target and left pointer number with right pointer number. Move right pointer if right
    value is greater, and move left pointer otherwise.

    Time complexity: O(n)
    Space complexity: O(1)
    """
    left, right = 0, len(numbers) - 1
    while left <= right:
        if numbers[right] > target - numbers[left]:
            right -= 1
        elif numbers[right] < target - numbers[left]:
            left += 1
        else:
            return [left + 1, right + 1]
    return []


if __name__ == '__main__':
    assert find_target_terms(numbers=[2, 7, 11, 15], target=9) == [1, 2]
    assert find_target_terms(numbers=[2, 3, 4], target=6) == [1, 3]
    assert find_target_terms(numbers=[-1, 0], target=-1) == [1, 2]
