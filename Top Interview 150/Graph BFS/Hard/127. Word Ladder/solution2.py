from collections import deque, defaultdict
from typing import List


def calc_min_words_chain(begin: str, end: str, words: List[str]) -> int:
    """
    BFS Approach.

    Define graph first:

             hit
       /      |      \
     *it     h*t     hi*
     /|\     /|\     /|\


    Time complexity: O(len(words))
    Space complexity: O(len(words))

    """
    if end not in words:
        return 0

    graph = defaultdict(list)
    for word in words:  # define graph
        for i in range(len(begin)):
            graph[word[:i] + "*" + word[i + 1:]].append(word)

    queue = deque([(begin, 1)])
    seen = {begin}
    while queue:
        word, n = queue.popleft()
        for i in range(len(begin)):
            pattern = word[:i] + "*" + word[i + 1:]
            for sample in graph[pattern]:
                if sample == end:
                    return n + 1

                if sample not in seen:
                    seen.add(sample)
                    queue.append((sample, n + 1))
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
