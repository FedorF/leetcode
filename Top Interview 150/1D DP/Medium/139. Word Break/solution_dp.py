from typing import List


def can_break(s: str, words: List[str]) -> bool:
    """
    DP Approach.


    Time complexity: O()
    Space complexity: O()

    where n is the length of s
    m is the maximum length of a word in the dictionary
    k is the total number of characters in all words in the dictionary
    """
    # todo!
    pass


if __name__ == '__main__':
    assert can_break(s="a", words=["a"]) is True
    assert can_break(s="a", words=["b"]) is False
    assert can_break(s="xxx", words=["xxx", "x"]) is True
    assert can_break(s="leetcode", words=["leet", "code"]) is True
    assert can_break(s="applepenapple", words=["apple", "pen"]) is True
    assert can_break(s="catsandog", words=["cats", "dog", "sand", "and", "cat"]) is False
