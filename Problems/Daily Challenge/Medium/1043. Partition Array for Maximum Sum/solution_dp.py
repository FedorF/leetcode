from typing import List


def calc_max_sum_partitioned(xs: List[int], k: int) -> int:
    """
    DP Approach with Round Robin storage.
    We need only k element in memory, so use Round Robin approach.

    Time complexity: O(len(xs) * k)
    Space complexity: O(k)

    """
    if k == 1:
        return sum(xs)

    if k >= len(xs):
        return len(xs) * max(xs)

    dp = [0] * k
    dp[0] = xs[0]
    for i in range(1, len(xs)):
        window_max_el = max_at_i = 0
        for j in range(i, i - k, -1):
            if j < 0:
                break

            window_max_el = max(window_max_el, xs[j])
            window_size = i + 1 - j
            cur_sum = window_max_el * window_size
            sub_sum = dp[(j - 1) % k] if j > 0 else dp[-1]
            max_at_i = max(max_at_i, cur_sum + sub_sum)
        dp[i % k] = max_at_i

    return dp[(len(xs) - 1) % k]


if __name__ == '__main__':
    actual, expected = calc_max_sum_partitioned(xs=[1, 15, 7, 9, 2, 5, 10], k=3), 84
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = calc_max_sum_partitioned(xs=[1, 4, 1, 5, 7, 3, 6, 1, 9, 9, 3], k=4), 83
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = calc_max_sum_partitioned(xs=[1], k=1), 1
    assert actual == expected, f"expected: {expected}, actual: {actual}"
