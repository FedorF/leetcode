from typing import List


def insert_interval(intervals: List[List[int]], new_interval: List[int]) -> List[List[int]]:
    """
    The idea is to find intervals that lie on the left/right side of new_interval (don't touch it);
    merge "middle" intervals that overlap with new one.


    Time complexity: O(n)
    Space complexity: O(n)

    """
    merged = False
    start, end = new_interval
    result = []
    for i in range(len(intervals)):
        cur_start, cur_end = intervals[i]
        if start >= cur_start and end <= cur_end:  # new_interval lies within current
            return intervals

        if (cur_end < start) or merged:  # current lies on the left/right side of new_interval
            result.append(intervals[i])
        else:  # process "middle" intervals
            if max(start, cur_start) <= min(end, cur_end):  # new_interval and current overlap
                start = min(start, cur_start)  # update start
                end = max(end, cur_end)  # and end
            else:  # we found first "right" interval; starting adding right intervals
                result.append([start, end])
                result.append(intervals[i])
                merged = True

    if not merged:  # new interval lies on the far right or covers all the intervals
        result.append([start, end])

    return result


if __name__ == '__main__':
    assert insert_interval(intervals=[[1, 3], [6, 9]], new_interval=[2, 5]) == [[1, 5], [6, 9]]
    assert insert_interval(
        intervals=[[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]],
        new_interval=[4, 8]
    ) == [[1, 2], [3, 10], [12, 16]]
    assert insert_interval(intervals=[], new_interval=[2, 5]) == [[2, 5]]
    assert insert_interval(intervals=[[1, 3], [6, 9]], new_interval=[0, 100]) == [[0, 100]]
    assert insert_interval(intervals=[[1, 5], [6, 9]], new_interval=[2, 7]) == [[1, 9]]
