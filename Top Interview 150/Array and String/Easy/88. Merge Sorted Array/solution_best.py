from typing import List


def merge_sorted_lists(xs: List[int], ys: List[int], m: int,  n: int) -> List[int]:
    """
    O(m+n) and constant space

    Start at the end and go to the beginning of each list.
    Compare elements from xs and ys and assign the bigger one to the current index k.
    """
    if m == 0:
        xs = ys[:]
        return xs
    if n == 0:
        return xs
    i = m-1
    j = n-1
    for k in range(m+n-1, -1, -1):
        if i < 0:
            xs[k] = ys[j]
            j -= 1
        elif j < 0:
            xs[k] = xs[i]
            i -= 1
        elif ys[j] > xs[i]:
            xs[k] = ys[j]
            j -= 1
        elif xs[i] >= ys[j]:
            xs[k] = xs[i]
            i -= 1
    return xs


if __name__ == '__main__':
    assert merge_sorted_lists([1, 2, 3, 0, 0, 0], [2, 5, 6], 3,  3) == [1, 2, 2, 3, 5, 6]
    assert merge_sorted_lists([1], [], 1, 0) == [1]
    assert merge_sorted_lists([0], [1], 0, 1) == [1]
    assert merge_sorted_lists([5, 0, 0, 0, 0], [1, 3, 4, 5], 1, 4) == [1, 3, 4, 5, 5]
