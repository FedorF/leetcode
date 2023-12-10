from typing import List


def can_break(s: str, words: List[str]) -> bool:
    """
    Depth-First Search with Memoization.
    Iterate through all the letters, and if word is found, there are two ways: continue, or run new search
    starting with next letter. Cache intermediate search.

    Time complexity: O(n * m + k)
    Space complexity: O(n + k)

    where n is the length of s
    m is the maximum length of a word in the dictionary
    k is the total number of characters in all words in the dictionary
    """
    words = set(words)
    cache = {}

    def dfs(start: int = 0):
        end = start + 1
        while end <= len(s):  # iterate till the end.
            if (start, end) in cache:
                return cache[(start, end)]

            if s[start:end] in words:  # found word
                if (end == len(s)) or dfs(end):  # start new search
                    cache[(start, end)] = True
                    return True
                else:
                    cache[(start, end)] = False
            end += 1
        return False

    return dfs()


if __name__ == '__main__':
    assert can_break(s="a", words=["a"]) is True
    assert can_break(s="a", words=["b"]) is False
    assert can_break(s="xxx", words=["xxx", "x"]) is True
    assert can_break(s="leetcode", words=["leet", "code"]) is True
    assert can_break(s="applepenapple", words=["apple", "pen"]) is True
    assert can_break(s="catsandog", words=["cats", "dog", "sand", "and", "cat"]) is False
