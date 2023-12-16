def find_longest_palindromic_substr(s: str) -> str:
    """
    Iterate through all elements and run palindromic search starting with current (pivot) element.
    We have to check both even and odd length palindromic substrings.


    Time Complexity: O(n^2)
    Space Complexity: O(1)

    """
    substr_ind = (0, 1)
    max_len = 1
    for i in range(1, len(s)):
        # check odd length
        cur_len = 1
        left, right = i - 1, i + 1
        while (left >= 0) and (right <= len(s) - 1) and (s[left] == s[right]):
            cur_len += 2
            if cur_len >= max_len:
                substr_ind = (left, right + 1)
                max_len = cur_len
            left -= 1
            right += 1

        # check even length
        cur_len = 0
        left, right = i - 1, i
        while (left >= 0) and (right <= len(s) - 1) and (s[left] == s[right]):
            cur_len += 2
            if cur_len >= max_len:
                substr_ind = (left, right + 1)
                max_len = cur_len
            left -= 1
            right += 1

    return s[substr_ind[0]:substr_ind[1]]


if __name__ == '__main__':
    assert find_longest_palindromic_substr(s="babad") == "aba"
    assert find_longest_palindromic_substr(s="cbbd") == "bb"
    assert find_longest_palindromic_substr(s="a") == "a"
    assert find_longest_palindromic_substr(s="xx") == "xx"
    assert find_longest_palindromic_substr(s="xxx") == "xxx"
    assert find_longest_palindromic_substr(s="xxxx") == "xxxx"
    assert find_longest_palindromic_substr(s="dxxx") == "xxx"
    assert find_longest_palindromic_substr(s="xxxd") == "xxx"
    assert find_longest_palindromic_substr(s="dxxxa") == "xxx"
    assert find_longest_palindromic_substr(s="dddddddd") == "dddddddd"
