import heapq
from typing import List


def find_k_largest(xs: List[int], k: int) -> int:
    """
    Use heapq module.

    Time complexity: O(n + k*log(n)) ~ O(n) if k << n
    Space complexity: O(n)
    """
    heapq.heapify(xs)
    return heapq.nlargest(k, xs)[-1]


if __name__ == '__main__':
    assert find_k_largest([3, 2, 1, 5, 6, 4], k=2) == 5
    assert find_k_largest([3, 2, 3, 1, 2, 4, 5, 5, 6], k=4) == 4
    assert find_k_largest([1], 1) == 1
    assert find_k_largest([7, 6, 5, 4, 3, 2, 1], 2) == 6
