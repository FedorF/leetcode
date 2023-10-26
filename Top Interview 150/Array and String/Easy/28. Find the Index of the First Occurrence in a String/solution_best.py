def find_first_occurrence(needle: str, haystack: str) -> int:
    """
    O(n) time complexity
    """
    return haystack.find(needle)


if __name__ == '__main__':
    assert find_first_occurrence("sad", "sadbutsad") == 0
    assert find_first_occurrence("leeto", "leetcode") == -1
