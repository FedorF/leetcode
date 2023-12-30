from collections import deque
from typing import List


def move_zeros(nums: List[int]):
    """
    Save vacant indexes in deque.


    Time complexity: O(n)
    Space complexity: O(n)

    """
    vacant_positions = deque()
    for i in range(len(nums)):
        if nums[i] == 0:
            vacant_positions.append(i)
        else:
            if len(vacant_positions) > 0:
                vacant = vacant_positions.popleft()
                nums[vacant], nums[i] = nums[i], 0
                vacant_positions.append(i)


if __name__ == '__main__':
    actual, expected = [0, 1, 0, 3, 12], [1, 3, 12, 0, 0]
    move_zeros(actual)
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = [0], [0]
    move_zeros(actual)
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = [111], [111]
    move_zeros(actual)
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = [1], [1]
    move_zeros(actual)
    assert actual == expected, f"expected: {expected}, actual: {actual}"
