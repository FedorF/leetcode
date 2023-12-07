from typing import List


def find_k_largest(xs: List[int], k: int) -> int:
    """
    Use QuickSort approach. split xs into partitions: less, equal, and greater than pivot element.
    Then, based on lengths of partitions and current k, pick certain partition and recursively run algo.

    Look at Readme.md for tree.

    Time complexity: O(n*log(n))
    Space complexity: O(n)
    """

    def search(nums: List[int], kth: int) -> int:
        if len(nums) == 1:
            return nums[0]

        least = greatest = nums[0]  # use first element as "pivot"
        less, equal, greater = [], [nums[0]], []
        for i in range(1, len(nums)):
            least = min(least, nums[i])
            greatest = max(greatest, nums[i])
            if nums[i] < nums[0]:
                less.append(nums[i])
            elif nums[i] > nums[0]:
                greater.append(nums[i])
            else:
                equal.append(nums[i])

        if kth == len(nums):  # edge case
            return least
        if kth == 1:  # edge case
            return greatest

        if kth <= len(greater):  # search kth in the "greater" partition
            return search(greater, kth)

        if kth > len(equal) + len(greater):  # search kth in "less" partition
            return search(less, kth - len(equal) - len(greater))

        return equal[0]  # search kth in "equal" partition

    return search(xs, k)


if __name__ == '__main__':
    assert find_k_largest([3, 2, 1, 5, 6, 4], k=2) == 5
    assert find_k_largest([3, 2, 3, 1, 2, 4, 5, 5, 6], k=4) == 4
    assert find_k_largest([1], 1) == 1
    assert find_k_largest([7, 6, 5, 4, 3, 2, 1], 2) == 6
