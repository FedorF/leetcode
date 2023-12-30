from typing import List


def calc_max_num_add_operations(xs: List[int], target: int) -> int:
    """
    Hashing approach. Count all the elements on the first run, then iterate through elements again and perform
    operation, if it's possible.


    Time complexity: O(n)
    Space complexity: O(n)

    """
    cache = {}
    for x in xs:
        if x in cache:
            cache[x] += 1
        elif x < target:
            cache[x] = 1

    res = 0
    for x in xs:
        if target == 2 * x:
            if cache[x] >= 2:
                res += 1
                cache[x] -= 2
            continue

        if (target - x in cache) and (cache[target - x] > 0) and (cache[x] > 0):
            res += 1
            cache[target - x] -= 1
            cache[x] -= 1

    return res


if __name__ == '__main__':
    actual, expected = calc_max_num_add_operations(xs=[1, 2, 3, 4], target=5), 2
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = calc_max_num_add_operations(xs=[3, 1, 3, 4, 3], target=6), 1
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = calc_max_num_add_operations(xs=[3], target=3), 0
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = calc_max_num_add_operations(xs=[3], target=10), 0
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = calc_max_num_add_operations(xs=[3, 7], target=20), 0
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = calc_max_num_add_operations(xs=[3, 7], target=10), 1
    assert actual == expected, f"expected: {expected}, actual: {actual}"
