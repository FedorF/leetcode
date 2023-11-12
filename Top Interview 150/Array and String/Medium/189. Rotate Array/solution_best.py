from typing import List


def rotate_list(xs: List[int], k: int):
    """
    Inplace version

    Time complexity: O(k+n)
    Space complexity: O(1)
    """
    k %= len(xs)
    if k > 0 and len(xs) > 1:
        xs[:-k], xs[-k:] = xs[-k:], xs[:-k]


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5, 6, 7]
    rotate_list(nums, 3)
    assert nums == [5, 6, 7, 1, 2, 3, 4]

    nums = [1, 2, 3, 4, 5, 6, 7]
    rotate_list(nums, 5)
    assert nums == [3, 4, 5, 6, 7, 1, 2]

    nums = [-1, -100, 3, 99]
    rotate_list(nums, 2)
    assert nums == [3, 99, -1, -100]

    nums = [100]
    rotate_list(nums, 1)
    assert nums == [100]

    nums = [100]
    rotate_list(nums, 2)
    assert nums == [100]
