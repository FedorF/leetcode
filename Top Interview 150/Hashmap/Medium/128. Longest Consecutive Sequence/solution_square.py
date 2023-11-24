from typing import List


def calc_max_consecutive_subseq_len(nums: List[int]) -> int:
    """
    Firstly, define set with all elements for O(1) look-up. Then walk through elements and try to build a subseq
    starting with current element.

    Warning: raises "Time Limit Exceeded" on leetcode test cases!

    Time complexity: O(n^2)
    Space complexity: O(n)
    """
    nums = set(nums)
    max_len = 0
    for x in nums:
        subseq_len = 0
        while x in nums:
            subseq_len += 1
            max_len = max(max_len, subseq_len)
            x += 1
    return max_len


if __name__ == '__main__':
    assert calc_max_consecutive_subseq_len([100, 4, 200, 1, 3, 2]) == 4
    assert calc_max_consecutive_subseq_len([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]) == 9
    assert calc_max_consecutive_subseq_len([]) == 0
    assert calc_max_consecutive_subseq_len([1]) == 1
