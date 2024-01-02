from typing import List


def find_difference(xs: List[int], ys: List[int]) -> List[List[int]]:
    """
    Cache both lists.


    Time complexity: O(n)
    Space complexity: O(n)

    """
    res = [[], []]
    xs_cache = set(xs)
    ys_cache = set(ys)
    for x in xs_cache:
        if x not in ys_cache:
            res[0].append(x)

    for y in ys_cache:
        if y not in xs_cache:
            res[1].append(y)

    return res


if __name__ == '__main__':
    actual, expected = find_difference([1, 2, 3], [2, 4, 6]), [[1, 3], [4, 6]]
    assert actual == expected, f"actual: {actual}, expected: {expected}"

    actual, expected = find_difference([1, 2, 3, 3], [1, 1, 2, 2]), [[3], []]
    assert actual == expected, f"actual: {actual}, expected: {expected}"

    actual, expected = find_difference([1], [1]), [[], []]
    assert actual == expected, f"actual: {actual}, expected: {expected}"

    actual, expected = find_difference([1, 2], [1]), [[2], []]
    assert actual == expected, f"actual: {actual}, expected: {expected}"

    actual, expected = find_difference([2], [1]), [[2], [1]]
    assert actual == expected, f"actual: {actual}, expected: {expected}"
