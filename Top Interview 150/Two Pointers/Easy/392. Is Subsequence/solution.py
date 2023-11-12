def is_subseq(s: str, t: str) -> bool:
    """
    Two pointers approach: one for subseq, second one for the string itself.

    Brute Force solution: O(len(t)).

    """
    if len(s) > len(t):
        return False

    if len(s) == 0:
        return True

    i = j = 0
    while (i < len(t)) and (j < len(s)):
        if s[j] == t[i]:
            if j == len(s)-1:
                return True
            j += 1
        i += 1
    return False


if __name__ == '__main__':
    assert is_subseq("abc", "ahbgdc") is True
    assert is_subseq("axc", "ahbgdc") is False
    assert is_subseq("", "ahbgdc") is True
    assert is_subseq("axc", "") is False
    assert is_subseq("", "") is True
    assert is_subseq("abcd", "abc") is False
