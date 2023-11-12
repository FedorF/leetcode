from typing import List


def find_ranges(nums: List[int]) -> List[str]:
    """
    Keep track of starting index. If condition is met, append new interval, and update starting index.

    Time complexity: O(N)
    Space complexity: O(N)
    """

    ranges = []
    interval_start = i = 0
    while i < len(nums):
        if i == len(nums) - 1:
            if i == interval_start:
                ranges.append(f"{nums[i]}")
            else:
                ranges.append(f"{nums[interval_start]}->{nums[i]}")
        else:
            if nums[i+1] - nums[i] > 1:
                if i == interval_start:
                    ranges.append(f"{nums[i]}")
                else:
                    ranges.append(f"{nums[interval_start]}->{nums[i]}")
                interval_start = i+1
        i += 1
    return ranges


if __name__ == '__main__':
    assert find_ranges([0, 1, 2, 4, 5, 7]) == ["0->2", "4->5", "7"]
    assert find_ranges([0, 2, 3, 4, 6, 8, 9]) == ["0", "2->4", "6", "8->9"]
    assert find_ranges([]) == []
