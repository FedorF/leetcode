from typing import List


def count_sublist_sum_eq(xs: List[int], target: int):
    """
    (See Readme.md)

    Space complexity: O(N)
    Time complexity: O(N)
    """
    sum_cnt = {0: 1}
    res, cur_sum = 0, 0
    for i in range(len(xs)):
        cur_sum += xs[i]  # Update current sum
        if cur_sum - target in sum_cnt:  # We have intermediate sub-array with needed sum
            res += sum_cnt[cur_sum - target]

        if cur_sum in sum_cnt:  # Update sum frequencies dict
            sum_cnt[cur_sum] += 1
        else:
            sum_cnt[cur_sum] = 1

    return res


if __name__ == "__main__":
    actual, expected = count_sublist_sum_eq([100], 1000), 0
    assert actual == expected, f"actual: {actual}\texpected: {expected}"

    actual, expected = count_sublist_sum_eq([100], 100), 1
    assert actual == expected, f"actual: {actual}\texpected: {expected}"

    actual, expected = count_sublist_sum_eq([1, 1, 1], 2), 2
    assert actual == expected, f"actual: {actual}\texpected: {expected}"

    actual, expected = count_sublist_sum_eq([1, 2, 3], 3), 2
    assert actual == expected, f"actual: {actual}\texpected: {expected}"
