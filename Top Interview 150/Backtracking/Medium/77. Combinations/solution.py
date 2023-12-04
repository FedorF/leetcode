from typing import List


def find_comb_with_new_value(val: int, combinations: List[List[int]]):
    """
    Add combinations of existing set and new value.
    Doesn't return anything, instead do it inplace.

    """
    k = len(combinations[0])
    for i in range(len(combinations)):
        for j in range(k):
            xs = combinations[i][:]
            xs[j] = val
            combinations.append(xs)


def find_combinations(n: int, k: int) -> List[List[int]]:
    if n == k:
        return [(list(range(n)))]
    comb = [[i for i in range(1, k + 1)]]
    print(comb)
    for val in range(k + 1, n + 1):
        find_comb_with_new_value(val, comb)
        print(val, comb)

    return comb


## todo!


if __name__ == '__main__':
    print(find_combinations(n=4, k=2))
    # assert find_combinations(n=4, k=2) == [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
    # assert find_combinations(n=1, k=1) == [[1]]
