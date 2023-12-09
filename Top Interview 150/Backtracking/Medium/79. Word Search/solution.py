from typing import List, Set, Tuple


def check_word(board: List[List[str]], word: str) -> bool:
    """
    Iterates through all possible starting letters and start dfs.
    Keep track of already seen elements in order not to use letter once.

    Time complexity: O(1)
    Space complexity: O(1)
    """

    n_rows, n_cols = len(board), len(board[0])

    def find_candidates(start: Tuple[int, int]) -> List[Tuple[int, int]]:
        """
        Finds all possible candidates of current element.

        Time complexity: O(4^(n*m)) ???
        Space complexity: O(len(word)) ~ O(1)
        """
        row, col = start
        candidates = []
        if col - 1 >= 0:
            candidates.append((row, col - 1))
        if col + 1 < n_cols:
            candidates.append((row, col + 1))
        if row - 1 >= 0:
            candidates.append((row - 1, col))
        if row + 1 < n_rows:
            candidates.append((row + 1, col))
        return candidates

    def start_search(word: str, start: Tuple[int, int], seen: Set[Tuple[int, int]]):
        row, col = start

        if (len(word) == 1) and (word[0] == board[row][col]):
            return True

        if word[0] != board[row][col]:
            return False

        seen.add(start)  # add current to history
        for candidate in find_candidates(start):
            if (candidate not in seen) and start_search(word[1:], candidate, seen):
                return True

        seen.remove(start)  # backtracking: remove current element from history
        return False

    for row in range(n_rows):
        for col in range(n_cols):
            if start_search(word, (row, col), set()):
                return True
    return False


if __name__ == '__main__':
    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    assert check_word(board, word="ABCCED") is True
    assert check_word(board, word="SEE") is True
    assert check_word(board, word="ABCB") is False
    assert check_word(board=[["A"]], word="A") is True
    assert check_word(board=[["a", "b"], ["c", "d"]], word="acdb") is True

    board = [["A", "B", "C", "E"], ["S", "F", "E", "S"], ["A", "D", "E", "E"]]
    assert check_word(board=board, word="ABCESEEEFS") is True
