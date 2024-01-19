def find_k_factor(n: int, k: int) -> int:
    """

    Time complexity: O(n)
    Space complexity: O(1)

    """
    if n <= 0:
        return -1

    factor, cnt = 1, 0
    while factor <= n // 2 and cnt <= k:
        if n % factor == 0:
            cnt += 1
            if cnt == k:
                return factor
        factor += 1

    if cnt + 1 == k:
        return n

    return -1


if __name__ == '__main__':
    actual, expected = find_k_factor(n=12, k=3), 3
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = find_k_factor(n=7, k=2), 7
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = find_k_factor(n=4, k=4), -1
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = find_k_factor(n=1, k=1), 1
    assert actual == expected, f"expected: {expected}, actual: {actual}"
