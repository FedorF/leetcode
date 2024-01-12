import heapq
from typing import List


def calc_max_score(xs: List[int], ys: List[int], k: int) -> int:
    """
    We can keep current subsequence elements in a min heap.


    Time complexity: O(n*log(n))
    Space complexity: O(n)

    """
    if k == len(xs):
        return sum(xs) * min(ys)

    # store elements pairs sorted by ys
    sorted_pairs = sorted(zip(xs, ys), key=lambda pair: pair[1], reverse=True)

    cur_subseq = []
    cur_sum = 0
    for i in range(k):  # initialize current sum and fill cur subseq heap with first k xs elements
        cur_sum += sorted_pairs[i][0]
        heapq.heappush(cur_subseq, sorted_pairs[i][0])

    max_score = cur_sum * sorted_pairs[k - 1][1]  # initialize max score by multiplying current sum by current min y
    for i in range(k, len(sorted_pairs)):  # run through the rest pairs
        x, y = sorted_pairs[i]
        # calc current best sum by adding new element (we have to) and subtracting minimal element from subsequence
        cur_sum += x - heapq.heapreplace(cur_subseq, x)
        max_score = max(max_score, cur_sum * y)  # update best score

    return max_score


if __name__ == '__main__':
    actual, expected = calc_max_score(xs=[1, 3, 3, 2], ys=[2, 1, 3, 4], k=3), 12
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = calc_max_score(xs=[4, 2, 3, 1, 1], ys=[7, 5, 10, 9, 6], k=1), 30
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = calc_max_score(xs=[1], ys=[2], k=1), 2
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = calc_max_score(xs=[1, 2, 3, 4, 5], ys=[1, 2, 3, 4, 5], k=5), 15
    assert actual == expected, f"expected: {expected}, actual: {actual}"
