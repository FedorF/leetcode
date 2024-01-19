from collections import Counter
from typing import List


def find_intersection(xs: List[int], ys: List[int]) -> List[str]:
    """


    Time complexity: O(len(xs) + len(ys))
    Space complexity: O(len(xs))

    """
    xs_cnt = Counter(xs)
    out = []
    for y in ys:
        if y in xs_cnt and xs_cnt[y] > 0:
            out.append(y)
            xs_cnt[y] -= 1

    return out


if __name__ == '__main__':
    actual, expected = find_intersection([1, 2, 2, 1], [2, 2]), [2, 2]
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = find_intersection([4, 9, 5], [9, 4, 9, 8, 4]), [9, 4]
    assert actual == expected, f"expected: {expected}, actual: {actual}"
