from typing import List


def calc_index(citations: List[int]) -> int:
    """
    Define dict where keys are citations and values are number of paper with corresponding number of citations.
    Due to the maximum possible h_index could be equal to total number of papers, we should limit our keys by the
    total number of papers. So, all the citations that are greater than the total number of papers will go to
    corresponding "bucket".
    Then we will walk through all possible h_indexes and return the right one.
    We have to check all possible h-indexes, because, for example in case [4, 4, 0, 0] h-index would be 2, so we'll
    check all possible values: 4, 3, 2, 1, 0

    Time complexity: O(n)
    Space complexity: O(n)
    """
    citations_cnt = {len(citations): 0}
    for x in citations:
        if x > len(citations):
            citations_cnt[len(citations)] += 1
        else:
            if x in citations_cnt:
                citations_cnt[x] += 1
            else:
                citations_cnt[x] = 1
    cnt = 0
    for i in range(len(citations), -1, -1):  # walk through all possible values of h-index
        cnt += citations_cnt.get(i, 0)  # for value that are not represented in dict, return 0.
        if cnt >= i:
            return i
    return 0


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
