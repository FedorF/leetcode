from typing import List


def find_powerset(xs: List[int]) -> List[List[int]]:
    """

    Time complexity: O(2^n)
    Space complexity: O(2^n)

    """
    powerset = [[]]
    for x in xs:  # run through all elements
        for i in range(len(powerset)):  # add current element to each already found subset
            s = powerset[i][:]  # make a copy of subset
            s.append(x)
            powerset.append(s)

    return powerset


if __name__ == '__main__':
    actual, expected = find_powerset([1, 2, 3]), [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
    assert actual == expected, f"actual: {actual}, expected: {expected}"

    actual, expected = find_powerset([0]), [[], [0]]
    assert actual == expected, f"actual: {actual}, expected: {expected}"
