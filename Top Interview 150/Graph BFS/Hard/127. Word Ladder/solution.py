from collections import deque
from typing import List


def calc_min_words_chain(begin: str, end: str, words: List[str]) -> int:
    """
    BFS Approach.


    Time complexity: O(len(words))
    Space complexity: O(len(words))

    """
    words = set(words)
    if end not in words:
        return 0

    seen = {begin}
    queue = deque([(begin, 1)])
    while queue:
        word, n = queue.popleft()
        if word == end:
            return n

        for i in range(len(begin)):  # run through all positions
            for c in "abcdefghijklmnopqrstuvwxyz":  # check every possible letter
                new_word = word[:i] + c + word[i + 1:]
                if new_word in words and new_word not in seen:
                    seen.add(new_word)
                    queue.append((new_word, n + 1))
    return 0


if __name__ == '__main__':
    actual, expected = calc_min_words_chain(
        "hit", "cog",
        ["hot", "dot", "dog", "lot", "log", "cog"]
    ), 5
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = calc_min_words_chain(
        "hit", "cog",
        ["hot", "dot", "dog", "lot", "log"]
    ), 0
    assert actual == expected, f"expected: {expected}, actual: {actual}"
