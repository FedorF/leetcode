def find_k_factor(n: int, k: int) -> int:
    """

    Time complexity: O(n)
    Space complexity: O(n)

    """
    if n <= 0:
        return -1

    factors = []
    for i in range(1, n // 2):
        if n % i == 0:
            factors.append(i)
    factors.append(n)

    if k <= len(factors):
        return factors[k - 1]

    return -1


if __name__ == '__main__':
    actual, expected = find_k_factor(n=12, k=3), 3
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = find_k_factor(n=7, k=2), 7
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = find_k_factor(n=4, k=4), -1
    assert actual == expected, f"expected: {expected}, actual: {actual}"
