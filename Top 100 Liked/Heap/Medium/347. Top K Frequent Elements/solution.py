import heapq
from typing import List


def top_freq_elements(xs: List[int], k: int) -> List[int]:
    """
    1) Calculate frequencies
    2) Define and fill heap of size k by push+popping elements from frequencies

    Time complexity: O(n)
    Space complexity: O(n)
    """
    if k >= len(xs):
        return xs

    freq = {}
    for i in range(len(xs)):
        if xs[i] in freq:
            freq[xs[i]] += 1
        else:
            freq[xs[i]] = 1

    top = []
    for el in freq:
        if len(top) < k:
            heapq.heappush(top, (freq[el], el))
        else:
            heapq.heappushpop(top, (freq[el], el))

    return [x[1] for x in top]


if __name__ == '__main__':
    actual, expected = top_freq_elements([5, 2, 5, 3, 5, 3, 1, 1, 3], 2), [3, 5]
    assert actual == expected, f"actual: {actual}, expected: {expected}"

    actual, expected = top_freq_elements([1, 1, 1, 2, 2, 3], 2), [2, 1]
    assert actual == expected, f"actual: {actual}, expected: {expected}"

    actual, expected = top_freq_elements([1], 1), [1]
    assert actual == expected, f"actual: {actual}, expected: {expected}"
