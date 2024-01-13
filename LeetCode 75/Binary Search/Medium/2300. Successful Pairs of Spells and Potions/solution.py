from typing import List


def successful_pairs(spells: List[int], potions: List[int], success: int) -> List[int]:
    """
    The brute force solution is to calculate cartesian product of spells and potions and check if each element is
    equal or greater than success. Therefore, the time complexity of such approach will be O(n*m).

    Better approach is to sort potions first (that will take O(m*log(m)) complexity). Then run through every spell,
    calculate target value, that equal to success divided by spell. And find the left-most insertion index of target
    value in potions list. Potions starting with that index are appropriate for problem. For finding this index we
    should perform log(m) operations. So, for n spells we'll make n*log(m) operations.


    Time complexity: O((n+m)*log(m))
    Space complexity: O(n+m)

    """
    potions = sorted(potions)
    res = []
    for spell in spells:
        target = success / spell

        left, right = 0, len(potions)
        while left < right:
            mid = (left + right) // 2
            if target > potions[mid]:
                left = mid + 1
            else:
                right = mid

        res.append(len(potions) - left)

    return res


if __name__ == '__main__':
    actual, expected = successful_pairs(spells=[5, 1, 3], potions=[1, 2, 3, 4, 5], success=7), [4, 0, 3]
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = successful_pairs(spells=[3, 1, 2], potions=[8, 5, 8], success=16), [2, 0, 2]
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = successful_pairs(spells=[10], potions=[10], success=101), [0]
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = successful_pairs(spells=[10], potions=[10], success=102), [0]
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = successful_pairs(spells=[10], potions=[10], success=100), [1]
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = successful_pairs(spells=[10], potions=[10], success=99), [1]
    assert actual == expected, f"expected: {expected}, actual: {actual}"
