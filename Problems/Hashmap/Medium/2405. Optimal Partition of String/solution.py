def calc_num_partitions(s: str) -> int:
    """

    Time complexity: O(n)
    Space complexity: O(n)

    """
    cur = set()
    num = 1
    for letter in s:
        if letter in cur:
            cur = set()
            num += 1

        cur.add(letter)

    return num


if __name__ == '__main__':
    actual, expected = calc_num_partitions("abacaba"), 4
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = calc_num_partitions("ssssss"), 6
    assert actual == expected, f"expected: {expected}, actual: {actual}"
