from typing import List


def find_combinations(k: int, target_sum: int) -> List[List[int]]:
    """
    Optimize function by tracking current unused element in cache.

    Time complexity: O(C(9, k)) ???
    Space complexity: O(C(9, k)) ???

    where C(n,k) = !n / !(n-k) / !k
    """

    def backtrack(cur_comb: List[int], x: int = 1, cur_sum: int = 0):
        if len(cur_comb) == k - 1:  # we can check if target_sum - cur_sum in db
            if (target_sum - cur_sum) > cur_comb[-1] and (target_sum - cur_sum) in db:
                cur_comb.append(target_sum - cur_sum)
                res.append(cur_comb[:])
                cur_comb.pop()
            return

        for i in range(x, 10):
            if cur_sum <= target_sum:  # don't process current combination if cur_sum > target_sum
                cur_comb.append(i)
                db.remove(i)
                backtrack(cur_comb, i + 1, cur_sum + i)
                db.add(cur_comb.pop())

    db = set(range(1, 10))
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
