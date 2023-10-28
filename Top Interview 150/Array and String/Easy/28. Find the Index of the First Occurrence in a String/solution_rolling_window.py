def find_first_occurrence(needle: str, haystack: str) -> int:
    """
    Sliding Window solution.
    O(n*m) time complexity
    """
    n = len(haystack)
    m = len(needle)
    for i in range(n - m + 1):
        flag = False
        for j in range(m):
            if needle[j] != haystack[i + j]:
                flag = False
                break
            else:
                flag = True
        if flag:
            return i

    return -1


if __name__ == '__main__':
    assert find_first_occurrence("sad", "sadbutsad") == 0
    assert find_first_occurrence("leeto", "leetcode") == -1
    assert find_first_occurrence("sap", "asap") == 1
