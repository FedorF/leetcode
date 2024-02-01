from typing import List


def calc_median(xs: List[int]) -> float:
    if len(xs) % 2 > 0:
        return xs[len(xs) // 2]

    return (xs[len(xs) // 2] + xs[len(xs) // 2 - 1]) / 2


def calc_median_non_overlapping(less: List[int], greater: List[int]) -> float:
    m, n = len(less), len(greater)

    if (m + n) % 2 > 0:
        ind = (m + n) // 2
        if ind < m:
            return less[ind]
        else:
            return greater[ind - m]

    ind1, ind2 = (m + n) // 2 - 1, (m + n) // 2
    if ind1 < m:
        med1 = less[ind1]
    else:
        med1 = greater[ind1 - m]

    if ind2 < m:
        med2 = less[ind2]
    else:
        med2 = greater[ind2 - m]

    return (med1 + med2) / 2


def calc_median_sorted_lists(xs: List[int], ys: List[int]) -> float:
    """


    Time complexity: O(log(m+n))
    Space complexity: O()

    """
    if len(xs) == 0:
        return calc_median(ys)

    if len(ys) == 0:
        return calc_median(xs)

    if xs[-1] <= ys[0]:
        return calc_median_non_overlapping(xs, ys)

    if ys[-1] <= xs[0]:
        return calc_median_non_overlapping(ys, xs)

    ## todo: calc_median_overlapping


if __name__ == '__main__':
    assert calc_median_sorted_lists([1, 2], [3, 4]) == 2.5
    assert calc_median_sorted_lists([3, 4, 5], [1, 3]) == 3
    assert calc_median_sorted_lists([1, 2, 3], []) == 2
    assert calc_median_sorted_lists([1, 2, 3, 4], []) == 2.5
    assert calc_median_sorted_lists([1, 3], [2]) == 2

