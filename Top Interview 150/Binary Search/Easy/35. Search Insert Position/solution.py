from typing import List


def find_insert_position(nums: List[int], target) -> int:
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2

        if target == nums[mid]:
            return mid
        if target < nums[mid]:
            right = mid - 1
        else:
            left = mid + 1

    return left


if __name__ == '__main__':
    assert find_insert_position([], 10) == 0
    assert find_insert_position([99], 100) == 1
    assert find_insert_position([99], 0) == 0
    assert find_insert_position([1, 3, 5, 6], 5) == 2
    assert find_insert_position([1, 3, 5, 6], 2) == 1
