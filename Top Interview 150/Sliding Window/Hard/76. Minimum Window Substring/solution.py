def find_min_window_substr_len(s: str, t: str) -> str:
    """
    Sliding window approach with two pointers.
    (See Readme.md)


    Time complexity: O(len(s))
    Space complexity: O(len(t))

    """
    if len(s) < len(t):
        return ""

    basis, used = {}, {}
    for letter in t:  # initiate basis and used dictionaries
        if letter in basis:
            basis[letter] += 1
        else:
            basis[letter] = 1

        if letter not in used:
            used[letter] = 0

    w_left, w_right, min_len = 0, 1, len(s) + 1  # initiate resulting window borders and length
    left = right = n_used_letters = 0
    while left < len(s):
        if n_used_letters == len(t):  # move left
            if right - left < min_len:  # update resulting window borders
                min_len = right - left
                w_left, w_right = left, right

            if s[left] in used:
                used[s[left]] -= 1
                if used[s[left]] < basis[s[left]]:
                    n_used_letters -= 1
            left += 1

        elif right >= len(s):  # right pointer has reached right border of s => move left
            left += 1

        else:  # move right
            if s[right] in basis:
                if used[s[right]] < basis[s[right]]:
                    n_used_letters += 1
                used[s[right]] += 1
            right += 1

    if min_len < len(s) + 1:
        return s[w_left:w_right]

    return ""


if __name__ == '__main__':
    actual, expected = find_min_window_substr_len(s="a", t="b"), ""
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = find_min_window_substr_len(s="a", t="a"), "a"
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = find_min_window_substr_len(s="ab", t="b"), "b"
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = find_min_window_substr_len(s="ADOBECODEBANC", t="ABC"), "BANC"
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = find_min_window_substr_len(s="a", t="aa"), ""
    assert actual == expected, f"expected: {expected}, actual: {actual}"
