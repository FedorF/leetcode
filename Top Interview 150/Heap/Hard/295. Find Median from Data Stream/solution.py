import heapq


class MedianFinder:
    """
    Use 2 heaps: maxheap - for smallest values, minheap - for greatest.
    There are two cases:
       1. We have odd total number of elements: [maxheap] median [minheap].
         1.1. In order to put new value, we can compare it with median and put smaller value to maxheap and bigger to
         minheap.
         1.2. In order to extract median, we can just return median.

       2. We have even total number of elements: [maxheap] [minheap].
         2.1. In order to put new value, we can compare it with max value from maxheap and min value from minheap.
         Leave one of these three element as median, and put other two into heaps (to obtain 1 case).
         2.2. In order to extract median, we can find average of max value from maxheap and min value from minheap

    (Everywhere in the implementation use negative values when dealing with left partition (maxheap), because python
    heapq module implemented as minheap.)


    Space complexity: O(n)

    """

    def __init__(self):
        self.left_part, self.right_part = [], []
        self.median = None
        self.is_first_num = True

    def addNum(self, num: int) -> None:
        """
        Time complexity: O(log(n))

        """
        if self.is_first_num:
            self.median = num
            self.is_first_num = False
            return

        if self.median is None:
            self.median = -heapq.heappushpop(self.left_part, -num)
            self.median = heapq.heappushpop(self.right_part, self.median)
            return

        if num <= self.median:
            heapq.heappush(self.left_part, -num)
            heapq.heappush(self.right_part, self.median)
        else:
            heapq.heappush(self.left_part, -self.median)
            heapq.heappush(self.right_part, num)
        self.median = None

    def findMedian(self) -> float:
        """
        Time complexity: O(1)

        """
        if self.median is not None:
            return self.median

        max_left = -self.left_part[0]
        min_right = self.right_part[0]

        return (min_right + max_left) / 2


def run_test(commands, xs):
    """
    Function for testing MedianFinder implementation.

    """
    min_stack = MedianFinder()
    res = []
    for i in range(len(commands)):
        if xs[i]:
            res.append(getattr(min_stack, commands[i])(xs[i][0]))
        else:
            res.append(getattr(min_stack, commands[i])())

    return res


if __name__ == '__main__':
    actual = run_test(["addNum", "addNum", "findMedian"], [[0], [0], []])
    expected = [None, None, 0]
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual = run_test(["addNum", "addNum", "findMedian", "addNum", "findMedian"], [[1], [2], [], [3], []])
    expected = [None, None, 1.5, None, 2.0]
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual = run_test(
        ["addNum", "findMedian", "addNum", "findMedian", "addNum",
         "findMedian", "addNum", "findMedian", "addNum", "findMedian"],
        [[-1], [], [-2], [], [-3], [], [-4], [], [-5], []]
    )
    expected = [None, -1.0, None, -1.5, None, -2.0, None, -2.5, None, -3.0]
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual = run_test(
        [
            "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian",
            "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian",
            "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian"],
        [[6], [], [10], [], [2], [], [6], [], [5], [], [0], [], [6], [], [3], [], [1], [], [0], [], [0], []]
    )
    expected = [
        None, 6., None, 8., None, 6., None, 6., None, 6., None,
        5.5, None, 6., None, 5.5, None, 5., None, 4., None, 3.]
    assert actual == expected, f"expected: {expected}, actual: {actual}"
