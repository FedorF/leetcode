from collections import deque
from typing import List


def remove_element(y: int, xs: List[int]) -> int:
    """
    Let's make stash list with indexes that we should swap.
    Using deque because popleft has constant time. Otherwise, if using list.pop(0), would linear time.

    O(N) time complexity
    O(N) space complexity
    """
    stash, k = deque(), 0
    for i, x in enumerate(xs):
        if x == y:
            stash.append(i)
        else:
            if len(stash) > 0:
                free_pos = stash.popleft()
                xs[free_pos] = x
                stash.append(i)
                xs[i] = y
            k += 1
    return k


if __name__ == '__main__':
    y = 3
    xs = [3, 2, 2, 3]
    k = remove_element(y, xs)
    assert (k == 2) and xs == [2, 2, 3, 3]

    y = 2
    xs = [0, 1, 2, 2, 3, 0, 4, 2]
    k = remove_element(y, xs)
    assert (k == 5) and xs == [0, 1, 3, 0, 4, 2, 2, 2]

    y = 1
    xs = [1]
    k = remove_element(y, xs)
    assert (k == 0) and xs == [1]

    y = 1
    xs = [0]
    k = remove_element(y, xs)
    assert (k == 1) and xs == [0]
