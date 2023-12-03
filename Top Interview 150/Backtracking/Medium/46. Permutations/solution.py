from typing import List


def find_permutations(xs: List[int]) -> List[List[int]]:
    if len(xs) == 1:
        return [xs]

    if len(xs) == 2:
        return [xs, [xs[1], xs[0]]]

    result = []
    for i in range(len(xs)):
        for shuffle in find_permutations(xs[:i] + xs[i + 1:]):
            result.append([xs[i]] + shuffle)
    return result


if __name__ == '__main__':
    assert find_permutations([1, 2, 3]) == [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    assert find_permutations([0, 1]) == [[0, 1], [1, 0]]
    assert find_permutations([1]) == [[1]]
