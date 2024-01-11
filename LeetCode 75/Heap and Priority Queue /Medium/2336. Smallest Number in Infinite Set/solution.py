import heapq
from typing import List


class SmallestInfiniteSet:
    """
    The idea is to keep elements in heap. The description says that num <= 1000, so we'll keep 1000 elements.
    And also we'll keep popped elements in set, in order to make fast (O(1)) check, if we should push element back to
    heap.

    """
    def __init__(self, max_element=1000):
        self.popped = set()
        self.heap = [x for x in range(1, max_element + 1)]

    def pop_smallest(self) -> int:
        """

        Time complexity: O(log(n))
        Space complexity: O(n), where n equals to max_element

        """
        smallest = heapq.heappop(self.heap)
        self.popped.add(smallest)
        return smallest

    def add_back(self, num: int):
        """

        Time complexity: O(log(n))
        Space complexity: O(n), where n equals to max_element

        """
        if num in self.popped:
            self.popped.remove(num)
            heapq.heappush(self.heap, num)


def run_test(xs: List[int]) -> List[int]:
    """

    Time complexity: O(n * log(n))
    Space complexity: O(n)

    """
    set_ = SmallestInfiniteSet()

    res = []
    for x in xs:
        if x == -1:
            res.append(set_.pop_smallest())
        else:
            set_.add_back(x)
    return res


if __name__ == '__main__':
    actual, expected = run_test([2, -1, -1, -1, 1, -1, -1, -1]), [1, 2, 3, 1, 4, 5]
    assert actual == expected, f"expected: {expected}, actual: {actual}"
