from typing import List


def has_unique_el_counts(xs: List[int]) -> bool:
    """

    Time complexity: O(n)
    Space complexity: O(n)

    """
    cnt = {}
    for x in xs:
        if x in cnt:
            cnt[x] += 1
        else:
            cnt[x] = 1

    occurrences = set(cnt.values())
    return len(occurrences) == len(cnt.keys())


if __name__ == '__main__':
    actual, expected = has_unique_el_counts([1, 2, 2, 1, 1, 3]), True
    assert actual == expected, f"actual: {actual}, expected: {expected}"

    actual, expected = has_unique_el_counts([1, 2]), False
    assert actual == expected, f"actual: {actual}, expected: {expected}"

    actual, expected = has_unique_el_counts([-3, 0, 1, -3, 1, 1, 1, -3, 10, 0]), True
    assert actual == expected, f"actual: {actual}, expected: {expected}"

    actual, expected = has_unique_el_counts([100]), True
    assert actual == expected, f"actual: {actual}, expected: {expected}"

    actual, expected = has_unique_el_counts([3, 5, -2, -3, -6, -6]), False
    assert actual == expected, f"actual: {actual}, expected: {expected}"
