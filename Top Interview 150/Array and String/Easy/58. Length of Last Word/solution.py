def find_last_word_len(s: str) -> int:
    """
    Time complexity: O(N).
    Because:
        s.split() = O(N)
        xs[-1] = O(1)
        len(s) = O(1)
    """
    return len(s.split()[-1])


if __name__ == '__main__':
    assert find_last_word_len("Hello World") == 5
    assert find_last_word_len("   fly me   to   the moon  ") == 4
    assert find_last_word_len("luffy is still joyboy") == 6
