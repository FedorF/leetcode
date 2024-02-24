from typing import List


class BoardTrie:
    """
    Builds Prefix Tree based on n*m matrix.

    """

    def __init__(self):
        self.children = {}

    def fit(self, board: List[List[str]]):
        """

        Time complexity: O((m*n)!)
        Space complexity: O((m*n)!)

        """
        n_rows, n_cols = len(board), len(board[0])

        def backtrack(row, col, node):
            for x, y in [(row, col - 1), (row, col + 1), (row - 1, col), (row + 1, col)]:
                if (0 <= x < n_rows) and (0 <= y < n_cols) and (x, y) not in used:
                    letter = board[x][y]
                    if letter not in node.children:
                        node.children[letter] = BoardTrie()

                    used.add((x, y))
                    backtrack(x, y, node.children[letter])
                    used.remove((x, y))

        for row in range(n_rows):
            for col in range(n_cols):
                if board[row][col] not in self.children:
                    self.children[board[row][col]] = BoardTrie()

                used = {(row, col)}
                backtrack(row, col, self.children[board[row][col]])

    def search(self, word: str) -> bool:
        """

        Time complexity: O(log(n_nodes))
        Space complexity: O(1)

        """
        node = self
        for c in word:
            if c not in node.children:
                return False
            node = node.children[c]
        return True


def find_words(board: List[List[str]], words: List[str]) -> List[str]:
    """
    1. Build a trie based on board
    2. Run through words and check if word in the trie

    Raises TLE!


    Time complexity: O((m*n)!)
    Space complexity: O((m*n)!)

    """
    trie = BoardTrie()
    trie.fit(board)
    res = []
    for word in words:
        if trie.search(word):
            res.append(word)

    return res


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
    actual, expected = find_words(board, words), ["oath", "eat"]
    assert actual == expected, f"expected: {expected}, actual: {actual}"
