import heapq
from typing import List


def find_smallest_sum_pairs(xs: List[int], ys: List[int], k: int) -> List[List[int]]:
    """
    Take the fact that xs and ys are sorted into account.
    1) Define heap and fill it with pairs of xs and ys[0]
    2) Iterate while k > 0 and pop smallest element from heap. Add smallest to result, and replace it with new pair.
    The new pair would be current x and next element in ys.

    Complexity: N + k*(log(N) + log(N)) = N + 2*k*log(N)

    Time complexity: O(k*log(N))
    Space complexity: O(N)
    """
    heap = []
    heapq.heapify(heap)
    for x in xs:  # fill heap with elements from xs and first element from ys
        heapq.heappush(heap, (x + ys[0], [x, 0]))

    res = []
    while heap and (k > 0):
        _, (x, ind_y) = heapq.heappop(heap)  # pull smallest element from heap
        res.append([x, ys[ind_y]])
        if ind_y < len(ys) - 1:  # if we have enough elements in ys
            heapq.heappush(heap, (x + ys[ind_y + 1], [x, ind_y + 1]))  # push next element from ys in heap
        k -= 1
    return res


if __name__ == '__main__':
    assert find_smallest_sum_pairs(xs=[1, 7, 11], ys=[2, 4, 6], k=3) == [[1, 2], [1, 4], [1, 6]]
    assert find_smallest_sum_pairs(xs=[1, 1, 2], ys=[1, 2, 3], k=2) == [[1, 1], [1, 1]]
    assert find_smallest_sum_pairs(xs=[1, 2], ys=[3], k=3) == [[1, 3], [2, 3]]
