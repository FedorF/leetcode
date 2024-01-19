from typing import List


def plus_one(nums: List[int]) -> List[int]:
    """

    Time complexity: O(n)
    Space complexity: O(1)

    """
    add_flag = True
    ind = len(nums) - 1
    while add_flag and ind >= 0:
        if nums[ind] == 9:
            nums[ind] = 0
            ind -= 1
        else:
            nums[ind] += 1
            add_flag = False

    if add_flag and ind < 0:
        nums = [1] + nums

    return nums


if __name__ == '__main__':
    actual, expected = plus_one([1, 2, 3]), [1, 2, 4]
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = plus_one([9]), [1, 0]
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = plus_one([1, 9, 9]), [2, 0, 0]
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = plus_one([9, 9, 9]), [1, 0, 0, 0]
    assert actual == expected, f"expected: {expected}, actual: {actual}"
