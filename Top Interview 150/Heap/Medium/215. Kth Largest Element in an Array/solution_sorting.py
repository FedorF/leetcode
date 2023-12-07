from typing import List


def find_k_largest(xs: List[int], k: int) -> int:
    """
    Sort list and return k largest.

    Time complexity: O(n*log(n))
    Space complexity: O(n)
    """
    return sorted(xs)[-k]


if __name__ == '__main__':
    assert find_k_largest([3, 2, 1, 5, 6, 4], k=2) == 5
    assert find_k_largest([3, 2, 3, 1, 2, 4, 5, 5, 6], k=4) == 4
    assert find_k_largest([1], 1) == 1
