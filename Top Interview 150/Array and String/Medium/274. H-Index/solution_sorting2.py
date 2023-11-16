from typing import List


def calc_index(citations: List[int]) -> int:
    """
    Sort input list reversely and walk through elements.
    If counter more or equal current value of citations, than return counter.

    Time complexity: O(n*log(n))
    Space complexity: O(1)
    """
    citations = sorted(citations, reverse=True)
    for i in range(len(citations)):
        if i >= citations[i]:
            return i
    return len(citations)


if __name__ == '__main__':
    assert calc_index([3, 0, 6, 1, 5]) == 3
    assert calc_index([1, 3, 1]) == 1
    assert calc_index([0]) == 0
    assert calc_index([10]) == 1
    assert calc_index([1]) == 1
    assert calc_index([1, 2]) == 1
    assert calc_index([4, 4, 0, 0]) == 2
    assert calc_index([4, 4, 1]) == 2
    assert calc_index([9, 7, 4, 1]) == 3
