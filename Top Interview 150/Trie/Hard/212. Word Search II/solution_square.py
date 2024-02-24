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


def find_words(board: List[List[str]], words: List[str]) -> List[str]:
    """
    1. Build a trie based on words
    2. Run through board and start dfs search from each letter in board to check if we can find word from trie


    Time complexity: O(m * n * log(n_nodes_in_trie))
    Space complexity: O(n_letters_in_words)

    """
    n_rows, n_cols = len(board), len(board[0])
    trie = Trie()
    for word in words:  # fit trie
        trie.insert(word)

    def backtrack(row: int, col: int, node: Trie, cur_word: str):
        if node.is_end:
            res.add(cur_word)

        for x, y in [(row, col - 1), (row, col + 1), (row - 1, col), (row + 1, col)]:
            if (0 <= x < n_rows) and (0 <= y < n_cols) and (board[x][y] in node.children):
                letter = board[x][y]
                board[x][y] = "*"
                backtrack(x, y, node.children[letter], cur_word + letter)
                board[x][y] = letter

    res = set()
    for row in range(n_rows):
        for col in range(n_cols):
            start_letter = board[row][col]
            if start_letter in trie.children:
                board[row][col] = "*"
                backtrack(row, col, trie.children[start_letter], start_letter)
                board[row][col] = start_letter

    return list(res)


if __name__ == '__main__':
    actual, expected = find_words([["a"]], ["a"]), ["a"]
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = find_words([["a", "a"]], ["aa"]), ["aa"]
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = find_words([["a", "b"], ["c", "d"]], ["abcb"]), []
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    board = [["o", "a", "a", "n"],
             ["e", "t", "a", "e"],
             ["i", "h", "k", "r"],
             ["i", "f", "l", "v"]]
    words = ["oath", "pea", "eat", "rain"]
    actual, expected1, expected2 = find_words(board, words), ["oath", "eat"], ["eat", "oath"]
    assert (actual == expected1) or (actual == expected2), f"expected: {expected1}, actual: {actual}"

    board = [["o", "a", "b", "n"],
             ["o", "t", "a", "e"],
             ["a", "h", "k", "r"],
             ["a", "f", "l", "v"]]
    words = ["oa", "oaa"]
    actual, expected1, expected2 = find_words(board, words), ["oa", "oaa"], ["oaa", "oa"]
    assert (actual == expected1) or (actual == expected2), f"expected: {expected1}, actual: {actual}"
