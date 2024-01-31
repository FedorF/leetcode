from collections import Counter
from typing import List


def find_all_concats(s: str, words: List[str]) -> List[int]:
    """
    Sliding window approach: use one pointer for keeping track on starting position, and other pointer for updating
    current word.
    (See Readme.md)


    Time complexity: O(len(s) * len(words) * len(word))
    Space complexity: O(len(words))

    """
    word_len, n = len(words[0]), len(words)
    if len(s) < word_len * n:
        return []

    db = Counter(words)
    used = {}
    left = right = concat_words_cnt = 0
    cur_word = ""
    res = []
    while left <= len(s) - word_len * n:  # run through all starting elements
        if cur_word in db:  # found current word in words
            if cur_word in used and used[cur_word] > 0:  # update current word occurrence in "used" dict
                used[cur_word] -= 1
                concat_words_cnt += 1
                cur_word = ""
            elif cur_word in used and used[cur_word] <= 0:  # we've already used current word
                cur_word = ""
                used = {}
                left += 1  # update starting point
                right = left
                concat_words_cnt = 0
            else:  # add current word to "used" dict
                used[cur_word] = db[cur_word] - 1
                concat_words_cnt += 1
                cur_word = ""
            continue

        if concat_words_cnt == n:  # found concatenation string occurrence in s
            res.append(left)
            used = {}
            left += 1  # update staring point
            right = left
            concat_words_cnt = 0
            continue

        if len(cur_word) < word_len:  # current word is not long enough
            cur_word += s[right]  # add next letter to current word
            right += 1
        else:  # current word is not in words => update staring point
            cur_word = ""
            used = {}
            left += 1
            right = left
            concat_words_cnt = 0

    return res


if __name__ == '__main__':
    actual, expected = find_all_concats(s="barfoothefoobarman", words=["foo", "bar"]), [0, 9]
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = find_all_concats(s="wordgoodgoodgoodbestword", words=["word", "good", "best", "word"]), []
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = find_all_concats(s="barfoofoobarthefoobarman", words=["bar", "foo", "the"]), [6, 9, 12]
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = find_all_concats(s="wordgoodgoodgoodbestword", words=["word", "good", "best", "good"]), [8]
    assert actual == expected, f"expected: {expected}, actual: {actual}"
