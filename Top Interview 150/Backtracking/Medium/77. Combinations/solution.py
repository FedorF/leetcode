from typing import List


def find_combinations_in_range(n: int, k: int) -> List[List[int]]:
    """
    At each step we're picking elements from elements that are greater than current.
    We'll stop picking process and add current combination to result if len(comb) == k


    Time complexity: O(k*C(n,k))
    Space complexity: O(k*C(n,k))

    where C(n,k) = n!/(n-k)!/k! is a number of combinations
    and k is operation of coping list of length k
    """
    res = []

    def backtrack(comb: List[int], start: int = 1):
        if len(comb) == k:
            res.append(comb[:])
            return

        for i in range(start, n + 1):
            comb.append(i)
            backtrack(comb, i + 1)
            comb.pop()

    backtrack([])
    return res


if __name__ == '__main__':
    assert find_combinations_in_range(n=4, k=2) == [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
    assert find_combinations_in_range(n=1, k=1) == [[1]]
