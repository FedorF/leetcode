from typing import List


def calc_max_avg_sublist(xs: List[int], k) -> float:
    """
    First of all, we should initialize first window and calculate it's average. In order to obtain new window sum,
    we can add new "right" element to current sum and subtract previous "left" element.

    Time complexity: O(n)
    Space complexity: O(1)

    """
    cur_sum = 0
    for i in range(k):  # initial window
        cur_sum += xs[i]
    max_avg = cur_sum / k

    left, right = 1, k
    while right < len(xs):
        cur_sum += xs[right] - xs[left - 1]
        if cur_sum / k > max_avg:
            max_avg = cur_sum / k
        left += 1
        right += 1

    return max_avg


if __name__ == '__main__':
    actual, expected = calc_max_avg_sublist(xs=[1, 12, -5, -6, 50, 3], k=4), 12.75
    assert abs(actual - expected) <= 1e-5, f"expected: {expected}, actual: {actual}"

    actual, expected = calc_max_avg_sublist(xs=[5], k=1), 5.0
    assert abs(actual - expected) <= 1e-5, f"expected: {expected}, actual: {actual}"

    actual, expected = calc_max_avg_sublist(xs=[1, 2, 3], k=1), 3.0
    assert abs(actual - expected) <= 1e-5, f"expected: {expected}, actual: {actual}"

    actual, expected = calc_max_avg_sublist(xs=[1, 2, 3], k=2), 2.5
    assert abs(actual - expected) <= 1e-5, f"expected: {expected}, actual: {actual}"

    actual, expected = calc_max_avg_sublist(xs=[1, 2, 3], k=3), 2.0
    assert abs(actual - expected) <= 1e-5, f"expected: {expected}, actual: {actual}"
