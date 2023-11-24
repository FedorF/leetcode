from typing import List


def merge_intervals(intervals: List[List[int]]) -> List[List[int]]:
    """
    Time complexity: O(n*log(n)), due to the sorting
    Space complexity: O(n)
    """
    if len(intervals) <= 1:
        return intervals

    intervals = sorted(intervals, key=lambda x: x[0])
    result = []
    cur_start, cur_end = intervals[0]
    for i in range(1, len(intervals)):
        if intervals[i][0] > cur_end:  # if current and previous intervals don't overlap:
            result.append([cur_start, cur_end])  # add current interval
            cur_start, cur_end = intervals[i]  # update current interval
        else:  # if overlap:
            cur_end = max(cur_end, intervals[i][1])  # update current interval's end

        if i == len(intervals) - 1:  # don't forget about the last interval
            result.append([cur_start, cur_end])

    return result


if __name__ == '__main__':
    assert merge_intervals([[2, 6], [1, 3], [8, 10], [15, 18]]) == [[1, 6], [8, 10], [15, 18]]
    assert merge_intervals([[1, 4], [4, 5]]) == [[1, 5]]
    assert merge_intervals([[1, 1]]) == [[1, 1]]
    assert merge_intervals([[1, 4], [2, 3]]) == [[1, 4]]
    assert merge_intervals([[1, 5], [2, 3], [3, 4], [6, 10]]) == [[1, 5], [6, 10]]
    assert merge_intervals([[2, 3], [4, 5], [6, 7], [8, 9], [1, 10]]) == [[1, 10]]
