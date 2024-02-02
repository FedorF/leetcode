from typing import List


def calc_median(nums: List[int]) -> float:
    """
    Calculates median of sorted list.


    Time complexity: O(1)
    Space complexity: O(1)

    """
    if len(nums) % 2 > 0:
        return nums[len(nums) // 2]

    return (nums[len(nums) // 2] + nums[len(nums) // 2 - 1]) / 2


def calc_median_non_overlapping(less: List[int], greater: List[int]) -> float:
    """
    Calculates median of sorted non overlapping list.


    Time complexity: O(1)
    Space complexity: O(1)

    """
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


def calc_median_overlapping(less: List[int], greater: List[int]) -> float:
    """
    Calculates median of sorted overlapping list.


    Time complexity: O(log(m+n))
    Space complexity: O(1)

    """

    m, n, total = len(less), len(greater), len(less) + len(greater)
    left, right = 0, m

    while True:
        i = left + (right - left) // 2
        j = (total + 1) // 2 - i

        less_max = float('-inf') if i == 0 else less[i - 1]
        greater_max = float('-inf') if j == 0 else greater[j - 1]
        less_min = float('inf') if i == m else less[i]
        greater_min = float('inf') if j == n else greater[j]

        if less_max <= greater_min and greater_max <= less_min:
            if total % 2 == 0:
                return (max(less_max, greater_max) + min(less_min, greater_min)) / 2
            else:
                return max(less_max, greater_max)

        elif less_max > greater_min:
            right = i - 1
        else:
            left = i + 1


def calc_median_sorted_lists(xs: List[int], ys: List[int]) -> float:
    """
    There are possible cases:
    1. One of list is empty
    2. Lists don't overlap
    3. Lists overlap

    (See Readme.md)


    Time complexity: O(log(m+n))
    Space complexity: O(1)

    """
    if len(xs) == 0:
        return calc_median(ys)

    if len(ys) == 0:
        return calc_median(xs)

    if xs[-1] <= ys[0]:
        return calc_median_non_overlapping(xs, ys)

    if ys[-1] <= xs[0]:
        return calc_median_non_overlapping(ys, xs)

    if len(xs) < len(ys):
        return calc_median_overlapping(xs, ys)

    return calc_median_overlapping(ys, xs)


if __name__ == '__main__':
    assert calc_median_sorted_lists([1, 2, 3, 5, 6], [4]) == 3.5
    assert calc_median_sorted_lists([1, 2], [3, 4]) == 2.5
    assert calc_median_sorted_lists([3, 4, 5], [1, 3]) == 3
    assert calc_median_sorted_lists([1, 2, 3], []) == 2
    assert calc_median_sorted_lists([1, 2, 3, 4], []) == 2.5
    assert calc_median_sorted_lists([1, 3], [2]) == 2
