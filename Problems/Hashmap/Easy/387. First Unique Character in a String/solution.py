def find_first_unique_letter(s: str) -> int:
    """

    Time complexity: O(n)
    Space complexity: O(n)

    """
    indexer = {}
    for i in range(len(s)):
        if s[i] in indexer:
            indexer[s[i]] = -1
        else:
            indexer[s[i]] = i

    min_ind = len(s)
    for letter, ind in indexer.items():
        if 0 <= ind < min_ind:
            min_ind = ind

    if min_ind < len(s):
        return min_ind

    return -1


if __name__ == '__main__':
    actual, expected = find_first_unique_letter("leetcode"), 0
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = find_first_unique_letter("loveleetcode"), 2
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = find_first_unique_letter("aabb"), -1
    assert actual == expected, f"expected: {expected}, actual: {actual}"
