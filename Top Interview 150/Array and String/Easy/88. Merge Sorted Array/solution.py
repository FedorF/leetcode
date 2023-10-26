from typing import List


def merge_sorted_lists(xs: List[int], ys: List[int], m: int,  n: int) -> List[int]:
    """
    Brute force solution O(2*(m+n)) and extra space.
    Create additional list
    """
    buffer = xs[:m]
    i = j = 0
    for x in range(m + n):
        if j == n:
            xs[x] = buffer[i]
            i += 1
        elif i == m:
            xs[x] = ys[j]
            j += 1
        else:
            a = buffer[i]
            b = ys[j]
            if a < b:
                xs[x] = a
                i += 1
            else:
                xs[x] = b
                j += 1
    return xs


if __name__ == '__main__':
    assert merge_sorted_lists([1, 2, 3, 0, 0, 0], [2, 5, 6], 3,  3) == [1, 2, 2, 3, 5, 6]
    assert merge_sorted_lists([1], [], 1, 0) == [1]
    assert merge_sorted_lists([0], [1], 0, 1) == [1]
    assert merge_sorted_lists([5, 0, 0, 0, 0], [1, 3, 4, 5], 1, 4) == [1, 3, 4, 5, 5]
