def find_longest_palindromic_substr(s: str) -> str:
    """
    Brute-forse solution.

    Raises "Time Limit Exceeded" error on leetcode.

    Time Complexity: O(n^3)
    Space Complexity: O(n^2)

    """
    dp = [[s[0]]]
    longest = s[0]
    for letter in range(1, len(s)):
        dp.append([s[letter]])
        i = 1
        for prev_substr in dp[letter - 1]:
            dp[letter].append(prev_substr + s[letter])
            if (dp[letter][i] == dp[letter][i][::-1]) and (len(dp[letter][i]) > len(longest)):  # check if palindromic
                longest = dp[letter][i]
            i += 1

    return longest


if __name__ == '__main__':
    assert find_longest_palindromic_substr(s="babad") == "bab"
    assert find_longest_palindromic_substr(s="cbbd") == "bb"
    assert find_longest_palindromic_substr(s="a") == "a"
    assert find_longest_palindromic_substr(s="xx") == "xx"
