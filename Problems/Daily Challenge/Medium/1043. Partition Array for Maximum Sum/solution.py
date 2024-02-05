from typing import List
from collections import deque


def calc_max_sum_partitioned(xs: List[int], k: int) -> int:
    """


    Time complexity: O()
    Space complexity: O()

    """
    ## todo:
    # https://www.youtube.com/watch?v=kWhy4ZUBdOY&t=52s

    cur_max_ind = 0
    dp = [0] * (len(xs) + 1)
    for i in range(len(dp)):
        if cur_max_ind + k < i + 1:
            pass
        if i >= k:
            dp[i] = max(dp[i - k] + xs[cur_max_ind] * k, xs[i] + xs[cur_max_ind] * k)


if __name__ == '__main__':
    actual, expected = calc_max_sum_partitioned(xs=[1, 15, 7, 9, 2, 5, 10], k=3), 84
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = calc_max_sum_partitioned(xs=[1, 4, 1, 5, 7, 3, 6, 1, 9, 9, 3], k=4), 83
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = calc_max_sum_partitioned(xs=[1], k=1), 1
    assert actual == expected, f"expected: {expected}, actual: {actual}"
