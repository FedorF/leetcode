from collections import deque
from typing import List


class RecentCounter:
    def __init__(self, ts_threshold=3000):
        self.requests = deque()
        self.ts_threshold = ts_threshold

    def ping(self, t: int) -> int:
        """
        Append new request.
        Run through all requests staring with first one and pop elements if they lie outside the period.
        Therefore, we'll save space and time.

        Time complexity: O(len(self.requests))
        Space complexity: O(len(self.requests))

        """
        self.requests.append(t)
        while len(self.requests) > 0 and self.requests[0] < t - self.ts_threshold:
            self.requests.popleft()

        return len(self.requests)


def count_pings(xs: List[int]) -> List[int]:
    """

    Time complexity: O(n)
    Space complexity: O(n)

    """
    counter = RecentCounter()
    for i in range(len(xs)):
        xs[i] = counter.ping(xs[i])
    return xs


if __name__ == '__main__':
    actual, expected = count_pings([1, 100, 3001, 3002]), [1, 2, 3, 3]
    assert actual == expected, f"expected: {expected}, actual: {actual}"
