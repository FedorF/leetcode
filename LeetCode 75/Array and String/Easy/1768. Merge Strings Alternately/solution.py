def merge_str(word1: str, word2: str) -> str:
    """
    Firstly add chars one after another; then fill rest chars.

    Time complexity: O(m+n)
    Space complexity: O(m+n)
    """
    last_ind = 0
    result = ""
    for a, b in zip(word1, word2):
        result += a
        result += b
        last_ind += 1

    if len(word1) > len(word2):
        for i in range(last_ind, len(word1)):
            result += word1[i]

    if len(word2) > len(word1):
        for i in range(last_ind, len(word2)):
            result += word2[i]

    return result


if __name__ == '__main__':
    assert merge_str(word1="abc", word2="pqr") == "apbqcr"
    assert merge_str(word1="ab", word2="pqrs") == "apbqrs"
    assert merge_str(word1="abcd", word2="pq") == "apbqcd"
    assert merge_str("a", "b") == "ab"
