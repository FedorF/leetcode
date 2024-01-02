from collections import Counter


def strings_are_close(xs: str, ys: str) -> bool:
    """
    Tricky approach. In order to check strings equality, we can check if strings have identical letter sets and also
    identical occurrences.

    For example,
    In the case when we have {a: 1, b: 2, c: 3} and {a: 3, b: 2, c: 1}, strings are close.


    Time complexity: O(n)
    Space complexity: O(n)

    """
    if len(xs) != len(ys):
        return False

    xs_cnt = Counter(xs)
    ys_cnt = Counter(ys)

    if xs_cnt.keys() != ys_cnt.keys():
        return False

    xs_occurrences = Counter(xs_cnt.values())
    ys_occurrences = Counter(ys_cnt.values())

    return xs_occurrences == ys_occurrences


if __name__ == '__main__':
    actual, expected = strings_are_close("aaabbbbccddeeeeefffff", "aaaaabbcccdddeeeeffff"), False
    assert actual == expected, f"actual: {actual}, expected: {expected}"

    actual, expected = strings_are_close("abbzzca", "babzzcz"), False
    assert actual == expected, f"actual: {actual}, expected: {expected}"

    actual, expected = strings_are_close("abc", "bca"), True
    assert actual == expected, f"actual: {actual}, expected: {expected}"

    actual, expected = strings_are_close("a", "aa"), False
    assert actual == expected, f"actual: {actual}, expected: {expected}"

    actual, expected = strings_are_close("cabbba", "abbccc"), True
    assert actual == expected, f"actual: {actual}, expected: {expected}"

    actual, expected = strings_are_close("a", "a"), True
    assert actual == expected, f"actual: {actual}, expected: {expected}"

    actual, expected = strings_are_close("a", "b"), False
    assert actual == expected, f"actual: {actual}, expected: {expected}"
