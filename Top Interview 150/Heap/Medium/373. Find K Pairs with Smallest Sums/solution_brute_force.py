import heapq
from typing import List


def find_smallest_sum_pairs(xs: List[int], ys: List[int], k: int) -> List[List[int]]:
    """
    Define heap of length k and heappushpop all possible pairs made from xs and ys. After this operation we'll have heap
    with k the smallest pairs. At the end sort heap and return result.
    Complexity: k + X*Y*log(k) + k*log(k) ~ X*Y*log(k)

    Time complexity: O(X*Y*log(k))
    Space complexity: O(k)


    !!! Raises "Time Limit Exceeded" on leetcode. !!!
    Because, this approach doesn't take the fact that input lists are sorted into account.
    """
    heap = []
    heapq.heapify(heap)
    for x in xs:
        for y in ys:
            if len(heap) < k:
                heapq.heappush(heap, (-(x + y), [x, y]))  # push negative sum in order to have "max-heap"
            else:
                heapq.heappushpop(heap, (-(x + y), [x, y]))  # push negative sum in order to have "max-heap"

    res = list(range((len(heap))))
    i = len(res) - 1
    while heap:
        res[i] = heapq.heappop(heap)[1]
        i -= 1
    return res


if __name__ == '__main__':
    a = find_smallest_sum_pairs(xs=[1, 2], ys=[3], k=3)
    assert find_smallest_sum_pairs(xs=[1, 7, 11], ys=[2, 4, 6], k=3) == [[1, 2], [1, 4], [1, 6]]
    assert find_smallest_sum_pairs(xs=[1, 1, 2], ys=[1, 2, 3], k=2) == [[1, 1], [1, 1]]
    assert find_smallest_sum_pairs(xs=[1, 2], ys=[3], k=3) == [[1, 3], [2, 3]]
