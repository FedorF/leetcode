from typing import List


class Trie:
    """
    Each node corresponds to certain letter, keeps its children nodes and has binary flag if it's an end of word.

    """

    def __init__(self):
        self.is_end = False
        self.children = {}

    def insert(self, word: str):
        """

        Time complexity: O(len(word))
        Space complexity: O(len(word))

        """
        node = self
        for c in word:
            if c not in node.children:
                node.children[c] = Trie()
            node = node.children[c]
        node.is_end = True

    def search(self, word: str) -> bool:
        """

        Time complexity: O(len(word))
        Space complexity: O(1)

        """
        node = self
        for c in word:
            if c not in node.children:
                return False
            node = node.children[c]

        return node.is_end

    def starts_with(self, prefix: str) -> bool:
        """

        Time complexity: O(len(word))
        Space complexity: O(1)

        """
        node = self
        for c in prefix:
            if c not in node.children:
                return False
            node = node.children[c]

        return True


def run_test(commands: List[str], words: List[str]):
    """

    Time complexity: O(len(words) * len(word))
    Space complexity: O(len(words) * len(word))

    """
    prefix_tree = Trie()
    res = []
    for i in range(len(commands)):
        output = getattr(prefix_tree, commands[i])(words[i])
        res.append(output)

    return res


if __name__ == '__main__':
    commands = ["insert", "search", "search", "starts_with", "insert", "search"]
    words = ["apple", "apple", "app", "app", "app", "app"]
    actual, expected = run_test(commands, words), [None, True, False, True, None, True]
    assert actual == expected, f"expected: {expected}, actual: {actual}"
