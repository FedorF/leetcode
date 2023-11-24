from typing import List


def calc_max_consecutive_subseq_len(nums: List[int]) -> int:
    """
    Firstly, sort nums than walk through and build subseq.

    Time complexity: O(n*log(n))
    Space complexity: O(n)
    """
    nums = sorted(set(nums))
    max_len = cur_len = 0
    for i in range(len(nums) - 1):
        cur_len += 1
        if nums[i] + 1 != nums[i + 1]:
            max_len = max(max_len, cur_len)
            cur_len = 0
    return max_len


if __name__ == '__main__':
    assert calc_max_consecutive_subseq_len([100, 4, 200, 1, 3, 2]) == 4
    assert calc_max_consecutive_subseq_len([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]) == 9
    assert calc_max_consecutive_subseq_len([]) == 0
    assert calc_max_consecutive_subseq_len([1]) == 1
