from typing import List


class Node:
    """
    Each node corresponds to certain letter, keeps its children nodes and has binary flag if it's an end of word.

    """

    def __init__(self):
        self.is_end = False
        self.children = {}


class WordDictionary:

    def __init__(self):
        self.trie = Node()

    def addWord(self, word: str) -> None:
        """

        Time complexity: O(len(word))
        Space complexity: O(len(word))

        """
        node = self.trie
        for c in word:
            if c not in node.children:
                node.children[c] = Node()
            node = node.children[c]
        node.is_end = True

    def search(self, word: str) -> bool:
        """

        Time complexity: O(n_nodes)
        Space complexity: O(1)

        """

        def dfs(node: Node, i: int = 0):
            if i >= len(word):
                return node.is_end

            if word[i] == ".":  # could be any letter
                if not node.children:
                    return False

                for c in node.children:  # so, iterate through all possible letters
                    if dfs(node.children[c], i + 1):
                        return True

            if word[i] in node.children:
                return dfs(node.children[word[i]], i + 1)

            return False

        return dfs(self.trie)


def run_test(commands: List[str], words: List[str]):
    word_dict = WordDictionary()
    res = []
    for i in range(len(commands)):
        output = getattr(word_dict, commands[i])(words[i])
        res.append(output)

    return res


if __name__ == '__main__':
    commands = ["addWord", "addWord", "addWord", "search", "search", "search", "search"]
    words = ["bad", "dad", "mad", "pad", "bad", ".ad", "b.."]
    actual, expected = run_test(commands, words), [None, None, None, False, True, True, True]
    assert actual == expected, f"expected: {expected}, actual: {actual}"
