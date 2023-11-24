from typing import List


def calc_max_consecutive_subseq_len(nums: List[int]) -> int:
    """
    In order to improve square time complexity, let's additionally check if current element is really a starting point.
    If there is an element less than current, then don't start loop for current element. Since, we check if smaller
    element is in set, we run "subseq" loop once, so algorithm improves to linear time.

    Time complexity: O(n)
    Space complexity: O(n)
    """
    nums = set(nums)
    max_len = 0
    for x in nums:
        if x - 1 in nums:  # this line improves time complexity to linear
            continue
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
