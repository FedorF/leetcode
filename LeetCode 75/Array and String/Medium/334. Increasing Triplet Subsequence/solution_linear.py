from typing import List


def exists_increasing_triplet(nums: List[int]) -> bool:
    """
    Define two additional list with minimal element on the left and maximum element on the right.
    Fill them in the first loop. And on the next loop check if triplet exists.
    See the picture in Readme.md

    Time complexity: O(n)
    Space complexity: O(n)

    """
    if len(nums) < 3:
        return False

    min_left, max_right = [0] * len(nums), [0] * len(nums)
    cur_min, cur_max = nums[0], nums[-1]
    left, right = 0, len(nums) - 1
    while right >= 0:  # fill min_left and max_right
        cur_min = min(cur_min, nums[left])
        min_left[left] = cur_min

        cur_max = max(cur_max, nums[right])
        max_right[right] = cur_max

        left += 1
        right -= 1

    for i in range(len(nums)):  # find triplet
        if min_left[i] < nums[i] < max_right[i]:
            return True

    return False


if __name__ == '__main__':
    actual, expected = exists_increasing_triplet(nums=[6, 7, 1, 2]), False
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = exists_increasing_triplet(nums=[1, 2, 3, 4, 5]), True
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = exists_increasing_triplet(nums=[5, 4, 3, 2, 1]), False
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = exists_increasing_triplet(nums=[2, 1, 5, 0, 4, 6]), True
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = exists_increasing_triplet(nums=[2, 1, 5]), False
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = exists_increasing_triplet(nums=[1, 2, 3]), True
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = exists_increasing_triplet(nums=[1, 2]), False
    assert actual == expected, f"expected: {expected}, actual: {actual}"
