from typing import List


def find_combinations(k: int, target_sum: int) -> List[List[int]]:
    """
    Brute force solution. For current x compose all possible combinations with length of k and numbers greater than x.

    Time complexity: O(C(9, k)) ???
    Space complexity: O(C(9, k)) ???

    where C(n,k) = !n / !(n-k) / !k
    """

    def backtrack(cur_comb: List[int], x: int = 1, cur_sum: int = 0):
        if len(cur_comb) == k:
            if cur_sum == target_sum:
                res.append(cur_comb[:])
            return

        for i in range(x, 10):
            cur_comb.append(i)
            backtrack(cur_comb, i + 1, cur_sum + i)
            cur_comb.pop()

    res = []
    backtrack([])
    return res


if __name__ == '__main__':
    actual, expected = find_combinations(3, 7), [[1, 2, 4]]
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = find_combinations(3, 9), [[1, 2, 6], [1, 3, 5], [2, 3, 4]]
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = find_combinations(4, 1), []
    assert actual == expected, f"expected: {expected}, actual: {actual}"
