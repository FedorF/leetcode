def reverse_words(s: str) -> str:
    """
    Built-in string function solution.

    Time complexity: O(n)
    Space complexity: O(n)
    """
    return " ".join(s.split()[::-1])


if __name__ == '__main__':
    assert reverse_words("the sky is blue") == "blue is sky the"
    assert reverse_words("  hello world  ") == "world hello"
    assert reverse_words("a good   example") == "example good a"
    assert reverse_words("s") == "s"
