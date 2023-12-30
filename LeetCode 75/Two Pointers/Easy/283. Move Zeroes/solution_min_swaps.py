from typing import List


def move_zeros(nums: List[int]):
    """
    Keep track on vacant position. If current element isn't equal to zero, swap this element with element on the vacant
    position, and update vacant position. Don't perform update with itself.

    Time complexity: O(n)
    Space complexity: O(1)

    """
    vacant_ind = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            if i != vacant_ind:
                nums[vacant_ind], nums[i] = nums[i], 0
            vacant_ind += 1


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
