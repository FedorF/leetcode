from typing import List


def remove_element(target: int, xs: List[int]) -> int:
    """
    Track the free position index and place element on it if it doesn't equal to target.
    At the same time that index would be a number of elements not equal to target.

    Time complexity: O(N)
    Space complexity: O(1)

    """
    free_pos = 0
    for i, x in enumerate(xs):
        if x != target:
            xs[free_pos] = x
            free_pos += 1
    return free_pos


if __name__ == '__main__':
    y = 10
    xs = [10, 2, 2, 10]
    k = remove_element(y, xs)
    assert (k == 2) and xs[:2] == [2, 2]

    y = 2
    xs = [0, 1, 2, 2, 3, 0, 4, 2]
    k = remove_element(y, xs)
    assert (k == 5) and xs[:5] == [0, 1, 3, 0, 4]

    y = 1
    xs = [1]
    k = remove_element(y, xs)
    assert (k == 0) and xs == [1]

    y = 1
    xs = [0]
    k = remove_element(y, xs)
    assert (k == 1) and xs == [0]

    y = 10
    xs = [10, 10]
    k = remove_element(y, xs)
    assert (k == 0) and xs == [10, 10]
