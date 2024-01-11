from typing import List


class RecentCounter:
    def __init__(self, ts_threshold=3000):
        self.requests = []
        self.ts_threshold = ts_threshold

    def ping(self, t: int) -> int:
        """
        Run through all previous requests starting with last one and count how many of them lie in period.
        Append new request in the end.


        Time complexity: O(len(self.requests))
        Space complexity: O(len(self.requests))

        """
        cnt = 1
        i = len(self.requests) - 1
        while i >= 0:
            if t <= self.requests[i] + self.ts_threshold:
                cnt += 1
                i -= 1
            else:
                break

        self.requests.append(t)
        return cnt


def count_pings(xs: List[int]) -> List[int]:
    """

    Time complexity: O(n^2)
    Space complexity: O(n)

    """
    counter = RecentCounter()
    for i in range(len(xs)):
        xs[i] = counter.ping(xs[i])
    return xs


if __name__ == '__main__':
    actual, expected = count_pings([1, 100, 3001, 3002]), [1, 2, 3, 3]
    assert actual == expected, f"expected: {expected}, actual: {actual}"
