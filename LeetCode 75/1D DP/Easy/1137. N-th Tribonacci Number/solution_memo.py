def find_tribonacci_number(n: int) -> int:
    """
    DFS with Memoization approach.


    Time complexity: O(n)
    Space complexity: O(n)

    """

    def func(x: int = n) -> int:
        if x == 0:
            return 0

        if x == 1 or x == 2:
            return 1

        if x in cache:
            return cache[x]

        cache[x] = func(x - 1) + func(x - 2) + func(x - 3)
        return cache[x]

    cache = {}
    return func()


if __name__ == '__main__':
    actual, expected = find_tribonacci_number(0), 0
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = find_tribonacci_number(4), 4
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = find_tribonacci_number(25), 1389537
    assert actual == expected, f"expected: {expected}, actual: {actual}"
