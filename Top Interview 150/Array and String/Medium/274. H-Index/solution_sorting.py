from typing import List


def calc_index(citations: List[int]) -> int:
    """
    Strange algorithmic solution, but works.

    Time complexity: O(n*log(n))
    Space complexity: O(1)
    """
    citations = sorted(citations, reverse=True)
    hindex = cnt = 0
    for i in range(len(citations)):
        cnt += 1
        hindex = max(hindex, min(citations[i], cnt))
    return hindex


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
