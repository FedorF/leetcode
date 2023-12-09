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

    def backtrack(comb: List[int], i: int = 0, total: int = 0):
        if total == target:
            res.append(comb[:])
            return

        if i >= len(candidates) or total > target:
            return

        comb.append(candidates[i])
        backtrack(comb, i, total + candidates[i])  # run left branch
        comb.pop()
        backtrack(comb, i + 1, total)  # run right branch

    backtrack([])
    return res


if __name__ == '__main__':
    assert find_combination_sum(candidates=[2, 3, 6, 7], target=7) == [[2, 2, 3], [7]]
    assert find_combination_sum(candidates=[2, 3, 5], target=8) == [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
    assert find_combination_sum(candidates=[2], target=1) == []
