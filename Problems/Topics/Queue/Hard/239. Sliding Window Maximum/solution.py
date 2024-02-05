from collections import deque
from typing import List


def sliding_window_max(xs: List[int], k: int) -> List[int]:
    """
    Monotonically decreasing queue approach.

    We want to have a monotonically decreasing queue at each step, so:
    1. Check that all elements in queue is inside current window
    2. Check that all elements in queue is greater than current element

    Time complexity: O(n)
    Space complexity: O(n)

    """
    res = []
    q = deque()  # keeps indexes
    for i in range(len(xs)):
        # remove element that are out of window from left end of the queue
        while q and q[0] + k <= i:
            q.popleft()

        # remove element that are less than current element from right end of the queue
        while q and xs[q[-1]] < xs[i]:
            q.pop()

        q.append(i)  # add current element
        if i + 1 >= k:  # we have enough element to form a window
            res.append(xs[q[0]])

    return res


if __name__ == '__main__':
    actual, expected = sliding_window_max([9, 10, 9, -7, -4, -8, 2, -6], 5), [10, 10, 9, 2]
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = sliding_window_max([1, 3, -1, -3, 5, 3, 6, 7], 3), [3, 3, 5, 5, 6, 7]
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = sliding_window_max(xs=[1, 15, 7, 9, 2, 5, 10], k=3), [15, 15, 9, 9, 10]
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = sliding_window_max(xs=[1], k=1), [1]
    assert actual == expected, f"expected: {expected}, actual: {actual}"
