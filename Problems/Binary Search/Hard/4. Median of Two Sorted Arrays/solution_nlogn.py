from typing import List


def calc_median(xs: List[int]) -> float:
    n = len(xs)
    if n == 1:
        return xs[0]

    elif n % 2 == 0:
        return (xs[int(n / 2)] + xs[int(n / 2) - 1]) / 2
    else:
        return xs[int(n / 2)]


def find_two_sorted_lists_median(xs: List[int], ys: List[int]) -> float:
    """

    Time complexity: O((n+m) * log(m+n))
    Space complexity: O(1)

    """
    if len(xs) == 0:
        return calc_median(ys)

    elif len(ys) == 0:
        return calc_median(xs)

    else:
        return calc_median(sorted(xs + ys))


if __name__ == '__main__':
    assert find_two_sorted_lists_median([1, 3], [2]) == 2
    assert find_two_sorted_lists_median([1, 2], [3, 4]) == 2.5

    # todo: improve complexity!
