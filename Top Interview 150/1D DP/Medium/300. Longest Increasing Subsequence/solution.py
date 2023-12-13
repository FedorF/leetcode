from typing import List


def find_longest_incr_subseq_len(nums: List[int]) -> int:
    """
    DP (bottom-up) approach.

    1) Start with last element. How many incr.subseq? Just 1, so dp[-1] = 1
    2) At each step iterate through all following elements, and if this element is greater, add current to this subseq
    and check if it's the longest one for current step.

    Keep track on global longest len.

    Time complexity: O(n^2)
    Space complexity: O(n)
    """

    dp = [1] * len(nums)
    global_max_len = 1
    for i in range(len(nums) - 2, -1, -1):
        for j in range(i + 1, len(nums)):
            if nums[j] > nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
        global_max_len = max(global_max_len, dp[i])

    return global_max_len


if __name__ == '__main__':
    assert find_longest_incr_subseq_len(nums=[10, 9, 2, 5, 3, 7, 101, 18]) == 4
    assert find_longest_incr_subseq_len(nums=[0, 1, 0, 3, 2, 3]) == 4
    assert find_longest_incr_subseq_len(nums=[7, 7, 7, 7, 7, 7, 7]) == 1
    assert find_longest_incr_subseq_len(nums=[100]) == 1
    assert find_longest_incr_subseq_len(nums=[1, 2, 3, 4, 5]) == 5
    assert find_longest_incr_subseq_len(nums=[5, 4, 3, 2, 1]) == 1
