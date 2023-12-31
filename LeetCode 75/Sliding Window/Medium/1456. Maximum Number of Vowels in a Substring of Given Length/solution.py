def max_vowels_substr(s: str, k: int) -> int:
    """
    Sliding window approach.


    Time complexity: O(n)
    Space complexity: O(1)

    """
    vowels = set("aeiou")

    max_vowels = 0
    for i in range(k):  # initial window
        if s[i] in vowels:
            max_vowels += 1

    window_cnt = max_vowels
    for i in range(k, len(s)):  # iterate through all the windows and keep track of window's vowels count
        if s[i] in vowels:  # check new right bound
            window_cnt += 1

        if s[i - k] in vowels:  # consider previous left bound
            window_cnt -= 1

        if window_cnt > max_vowels:  # update max count if needed
            max_vowels = window_cnt

    return max_vowels


if __name__ == '__main__':
    actual, expected = max_vowels_substr(s="abciiidef", k=3), 3
    assert actual == expected, f"actual: {actual}, expected: {expected}"

    actual, expected = max_vowels_substr(s="aeiou", k=2), 2
    assert actual == expected, f"actual: {actual}, expected: {expected}"

    actual, expected = max_vowels_substr(s="leetcode", k=3), 2
    assert actual == expected, f"actual: {actual}, expected: {expected}"

    actual, expected = max_vowels_substr(s="l", k=1), 0
    assert actual == expected, f"actual: {actual}, expected: {expected}"

    actual, expected = max_vowels_substr(s="a", k=1), 1
    assert actual == expected, f"actual: {actual}, expected: {expected}"

    actual, expected = max_vowels_substr(s="aaaa", k=3), 3
    assert actual == expected, f"actual: {actual}, expected: {expected}"
