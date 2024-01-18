from typing import List


def find_min_n_intervals_to_del(intervals: List[List[int]]) -> int:
    """
    Greedy approach. If two adjacent intervals overlaps, remove one with the greatest end, because it has greater
    chance to overlaps with the next one (see Readme.md).


    Time complexity: O(n * log(n))
    Space complexity: O(1)

    """
    intervals = sorted(intervals, key=lambda x: x[0])
    res = 0
    prev_st, prev_end = intervals[0]
    for i in range(1, len(intervals)):
        st, end = intervals[i]
        if min(prev_end, end) > max(prev_st, st):  # overlaps
            res += 1
            if end < prev_end:
                prev_st, prev_end = st, end
        else:  # don't overlaps
            prev_st, prev_end = st, end

    return res


if __name__ == '__main__':
    actual, expected = find_min_n_intervals_to_del([[1, 2], [2, 3], [3, 4], [1, 3]]), 1
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = find_min_n_intervals_to_del([[1, 2], [1, 2], [1, 2]]), 2
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = find_min_n_intervals_to_del([[1, 2], [2, 3]]), 0
    assert actual == expected, f"expected: {expected}, actual: {actual}"
