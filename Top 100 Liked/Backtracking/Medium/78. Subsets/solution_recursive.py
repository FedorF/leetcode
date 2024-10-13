from typing import List


def find_powerset(xs: List[int]) -> List[List[int]]:
    """

    Time complexity: O(2^n)
    Space complexity: O(2^n)

    """

    def backtrack(i: int = 0):
        nonlocal powerset, s
        if i >= len(xs):
            powerset.append(s[:])
            return

        # two options for current element
        backtrack(i + 1)  # included to the current subset

        s.append(xs[i])  # not include to the current subset
        backtrack(i + 1)
        s.pop()

        return

    powerset, s = [], []
    backtrack()
    return powerset


if __name__ == '__main__':
    actual, expected = find_powerset([1, 2, 3]), [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
    assert sorted(actual) == sorted(expected), f"actual: {actual}, expected: {expected}"

    actual, expected = find_powerset([0]), [[], [0]]
    assert sorted(actual) == sorted(expected), f"actual: {actual}, expected: {expected}"
