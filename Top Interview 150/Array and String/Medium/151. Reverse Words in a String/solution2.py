def reverse_words(s: str) -> str:
    """
    Algorithmic solution.

    Time complexity: O(n)
    Space complexity: O(n)
    """
    words = []
    new_word_flag = True
    for ch in s:
        if ch == " ":
            new_word_flag = True
        else:
            if new_word_flag:
                words.append(ch)
                new_word_flag = False
            else:
                words[-1] = words[-1] + ch

    s_reversed = ""
    for i in range(len(words)-1, -1, -1):
        s_reversed += words[i]
        if i > 0:
            s_reversed += " "
    return s_reversed


if __name__ == '__main__':
    assert reverse_words("the sky is blue") == "blue is sky the"
    assert reverse_words("  hello world  ") == "world hello"
    assert reverse_words("a good   example") == "example good a"
    assert reverse_words("s") == "s"
    assert reverse_words("EPY2giL") == "EPY2giL"
