from typing import List


def remove_duplicates(xs: List[int]) -> int:
    """
    Actually, there is no need for additional set with already seemed elements, because input list is sorted.
    So, we can compare current element with previous one. If it differs than we move current to vacant position, and
    update vacant position pointer by 1.

    Time complexity: O(N)
    Space complexity: O(1)
    """
    if len(xs) == 0:
        return 0

    free_pos = 1
    for i in range(free_pos, len(xs)):
        if xs[i] > xs[i - 1]:
            xs[free_pos] = xs[i]
            free_pos += 1

    return free_pos


if __name__ == '__main__':
    xs = [1, 1, 2]
    k = remove_duplicates(xs)
    assert (k == 2) and (xs[:2] == [1, 2])

    xs = [1, 2, 2]
    k = remove_duplicates(xs)
    assert (k == 2) and (xs[:2] == [1, 2])

    xs = [0, 0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    k = remove_duplicates(xs)
    assert (k == 5) and (xs[:5] == [0, 1, 2, 3, 4])

    xs = []
    k = remove_duplicates(xs)
    assert (k == 0) and (xs == [])

    xs = [100, 100]
    k = remove_duplicates(xs)
    assert (k == 1) and (xs[:1] == [100])

    xs = [10]
    k = remove_duplicates(xs)
    assert (k == 1) and (xs[:1] == [10])
