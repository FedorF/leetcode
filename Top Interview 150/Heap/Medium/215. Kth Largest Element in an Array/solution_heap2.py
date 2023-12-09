import heapq
from typing import List


def find_k_largest(xs: List[int], k: int) -> int:
    """
    Use heapq module.

    Time complexity: O(n*log(k))
    Space complexity: O(k)
    """
    top_largest = xs[:k]
    heapq.heapify(top_largest)
    for i in range(k, len(xs)):
        heapq.heappushpop(top_largest, xs[i])
    return top_largest[0]


if __name__ == '__main__':
    assert find_k_largest([3, 2, 1, 5, 6, 4], k=2) == 5
    assert find_k_largest([3, 2, 3, 1, 2, 4, 5, 5, 6], k=4) == 4
    assert find_k_largest([1], 1) == 1
    assert find_k_largest([7, 6, 5, 4, 3, 2, 1], 2) == 6
