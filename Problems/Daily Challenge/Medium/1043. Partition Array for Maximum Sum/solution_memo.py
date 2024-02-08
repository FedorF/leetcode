from typing import List


def calc_max_sum_partitioned(xs: List[int], k: int) -> int:
    """
    Memoization approach.


    Time complexity: O(len(xs)*k)
    Space complexity: O(len(xs))

    """
    if k == 1:
        return sum(xs)

    if k >= len(xs):
        return len(xs) * max(xs)

    cache = {}

    def dfs(left_bound: int = 0):
        if left_bound >= len(xs):
            return 0

        if left_bound in cache:
            return cache[left_bound]

        max_sum = window_max_el = 0
        for right_bound in range(left_bound, left_bound + k):
            if right_bound == len(xs):  # reached end of xs
                break

            window_max_el = max(window_max_el, xs[right_bound])  # find current max element in window
            window_size = right_bound + 1 - left_bound  # find current window size
            max_sum = max(max_sum, window_max_el * window_size + dfs(right_bound + 1))

        cache[left_bound] = max_sum
        return max_sum

    return dfs()


if __name__ == '__main__':
    actual, expected = calc_max_sum_partitioned(xs=[1, 15, 7, 9, 2, 5, 10], k=3), 84
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = calc_max_sum_partitioned(xs=[1, 4, 1, 5, 7, 3, 6, 1, 9, 9, 3], k=4), 83
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = calc_max_sum_partitioned(xs=[1], k=1), 1
    assert actual == expected, f"expected: {expected}, actual: {actual}"
