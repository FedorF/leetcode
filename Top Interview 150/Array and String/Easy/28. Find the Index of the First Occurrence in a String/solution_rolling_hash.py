def find_first_occurrence(needle: str, haystack: str) -> int:
    """
    Rabin Karp algorithm (Rolling Hash).
    O(n*m) time complexity
    """
    n = len(haystack)
    m = len(needle)
    needle_hash = hash(needle)
    for i in range(n-m+1):
        if hash(haystack[i:i+m]) == needle_hash:
            return i
    return -1


if __name__ == '__main__':
    assert find_first_occurrence("sad", "sadbutsad") == 0
    assert find_first_occurrence("leeto", "leetcode") == -1
    assert find_first_occurrence("sap", "asap") == 1
