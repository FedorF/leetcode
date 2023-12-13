from typing import List


def can_break(s: str, words: List[str]) -> bool:
    """
    DP Approach. Check Readme.md

    Time complexity: O(len(s) * len(words))
    Space complexity: O(len(s))

    """
    dp = [False] * len(s)
    dp.append(True)  # base case

    for i in range(len(s) - 1, -1, -1):  # iterate through all letters
        for word in words:  # match every word from dict
            if (i + len(word) <= len(s)) and (s[i:i + len(word)] == word):  # if we have enough letters and it's a match
                dp[i] = True and dp[i + len(word)]  # it's a match, but we also have to check if i + len(word) is ...
                if dp[i]:  # also a match
                    break  # we don't have to check rest words in dict
    return dp[0]


if __name__ == '__main__':
    assert can_break(s="a", words=["a"]) is True
    assert can_break(s="a", words=["b"]) is False
    assert can_break(s="xxx", words=["xxx", "x"]) is True
    assert can_break(s="leetcode", words=["leet", "code"]) is True
    assert can_break(s="applepenapple", words=["apple", "pen"]) is True
    assert can_break(s="catsandog", words=["cats", "dog", "sand", "and", "cat"]) is False
