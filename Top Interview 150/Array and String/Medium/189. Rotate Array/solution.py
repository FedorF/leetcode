from typing import List


def rotate_list(xs: List[int], k: int) -> List[int]:
    """
    Return new list version

    Time complexity: O(N)
    Space complexity: O(N)
    """
    k %= len(xs)
    if k == 0:
        return xs
    return xs[-k:] + xs[:-k]


if __name__ == '__main__':
    assert rotate_list([1, 2, 3, 4, 5, 6, 7], 3) == [5, 6, 7, 1, 2, 3, 4]
    assert rotate_list([1, 2, 3, 4, 5, 6, 7], 5) == [3, 4, 5, 6, 7, 1, 2]
    assert rotate_list([-1, -100, 3, 99], 2) == [3, 99, -1, -100]
    assert rotate_list([100], 1) == [100]
    assert rotate_list([100], 2) == [100]
