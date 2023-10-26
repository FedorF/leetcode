from typing import List


def remove_duplicates(xs: List[int]) -> int:
    """
    Linear time and constant space.
    We have to track elements that are already seemed in xs. So, let's make duplicated elements set.
    """
    seen = set()
    free_pos = 0
    for i, x in enumerate(xs):
        if x not in seen:
            seen.add(x)
            xs[free_pos] = x
            free_pos += 1
    return free_pos


if __name__ == '__main__':
    xs = [1, 1, 2]
    k = remove_duplicates(xs)
    assert (k == 2) and (xs[:2] == [1, 2])

    xs = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    k = remove_duplicates(xs)
    assert (k == 5) and (xs[:5] == [0, 1, 2, 3, 4])

    xs = []
    k = remove_duplicates(xs)
    assert (k == 0) and (xs == [])

    xs = [100, 100]
    k = remove_duplicates(xs)
    assert (k == 1) and (xs[:1] == [100])
