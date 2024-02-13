from typing import List


def get_suggestions(documents: List[str], query: str) -> List[List[str]]:
    """

    Time Complexity: O(m * n * log(m * n))
    Space Complexity: O(n)

    where n = len(documents), n = len(words in documents)
    """
    documents = sorted(documents)

    res = []
    left, right = 0, len(documents) - 1
    for i in range(len(query)):
        letter = query[i]
        while left <= right and (len(documents[left]) <= i or documents[left][i] != letter):
            left += 1

        while left <= right and (len(documents[right]) <= i or documents[right][i] != letter):
            right -= 1

        suggestions = []
        for j in range(left, min(left + 3, right + 1)):
            suggestions.append(documents[j])
        res.append(suggestions)

    return res


if __name__ == '__main__':
    expected = [["mobile", "moneypot", "monitor"],
                ["mobile", "moneypot", "monitor"],
                ["mouse", "mousepad"],
                ["mouse", "mousepad"],
                ["mouse", "mousepad"]]
    actual = get_suggestions(["mobile", "mouse", "moneypot", "monitor", "mousepad"], "mouse")
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    expected = [["havana"], ["havana"], ["havana"], ["havana"], ["havana"], ["havana"]]
    actual = get_suggestions(["havana"], "havana")
    assert actual == expected, f"expected: {expected}, actual: {actual}"
