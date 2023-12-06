from typing import List


def find_combination_sum(candidates: List[int], target: int) -> List[List[int]]:
    """
    The idea is to build a tree. On left branch we'll check all possible combinations including current element.
    On the right tree we'll check all possible combinations except current element.
    If total sum of current combination is greater than target than terminate.

    Time complexity: O(2^n)
    Space complexity: O(n)
    """
    res = []

    def backtrack(i, total, comb):
        if total == target:
            res.append(comb[:])
            return
        if i >= len(candidates) or total > target:
            return

        comb.append(candidates[i])
        backtrack(i, total + candidates[i], comb)  # left branch
        comb.pop()
        backtrack(i + 1, total, comb)  # right branch

    backtrack(0, 0, [])
    return res


if __name__ == '__main__':
    assert find_combination_sum(candidates=[2, 3, 6, 7], target=7) == [[2, 2, 3], [7]]
    assert find_combination_sum(candidates=[2, 3, 5], target=8) == [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
    assert find_combination_sum(candidates=[2], target=1) == []
