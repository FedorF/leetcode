from typing import List


def calc_median(xs: List[int]) -> float:
    if len(xs) % 2 > 0:
        return xs[len(xs) // 2]

    return (xs[len(xs) // 2] + xs[len(xs) // 2 - 1]) / 2


def calc_median_sorted_lists(xs: List[int], ys: List[int]) -> float:
    """
    Brute force solution.

    Time complexity: O((n+m) * log(m+n))
    Space complexity: O(1)

    """
    if len(xs) == 0:
        return calc_median(ys)

    if len(ys) == 0:
        return calc_median(xs)

    return calc_median(sorted(xs + ys))


if __name__ == '__main__':
    assert calc_median_sorted_lists([1, 3], [2]) == 2
    assert calc_median_sorted_lists([1, 2], [3, 4]) == 2.5
    assert calc_median_sorted_lists([1, 2, 3], []) == 2
    assert calc_median_sorted_lists([1, 2, 3, 4], []) == 2.5
