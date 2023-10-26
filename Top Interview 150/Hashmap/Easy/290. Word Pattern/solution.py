def is_pattern(pattern: str, sentence: str) -> bool:
    """
    Solution with additional zero step: split sentence to words.
    Time complexity: O(2*N)
    Space complexity: O(3*N)
    """

    sentence = sentence.split()
    if len(sentence) != len(pattern):
        return False

    straight = {}
    inverse = {}
    for i in range(len(sentence)):
        word_map = straight.get(pattern[i])
        char_map = inverse.get(sentence[i])
        if not word_map and not char_map:
            straight[pattern[i]] = sentence[i]
            inverse[sentence[i]] = pattern[i]
        elif word_map and char_map:
            if word_map != sentence[i] or char_map != pattern[i]:
                return False
        else:
            return False

    return True


if __name__ == '__main__':
    assert is_pattern("abba", "dog cat cat dog") is True
    assert is_pattern("abba", "dog cat cat fish") is False
    assert is_pattern("aaaa", "dog cat cat dog") is False
