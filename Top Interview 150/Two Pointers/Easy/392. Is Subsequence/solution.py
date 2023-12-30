def is_subseq(s: str, t: str) -> bool:
    """
    Two pointers approach: one for subseq, second one for the string itself.

    Time complexity: O(len(t))
    Space complexity: O(1)

    """
    if len(s) > len(t):
        return False

    j = i = 0
    while j < len(s) and i < len(t):
        if t[i] == s[j]:
            j += 1
        i += 1
    return j == len(s)


if __name__ == '__main__':
    assert is_subseq("abc", "ahbgdc") is True
    assert is_subseq("axc", "ahbgdc") is False
    assert is_subseq("", "ahbgdc") is True
    assert is_subseq("axc", "") is False
    assert is_subseq("", "") is True
    assert is_subseq("abcd", "abc") is False
