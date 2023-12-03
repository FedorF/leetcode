from typing import List


def find_combinations(x: List[str], y: List[str]) -> List[str]:
    """
    Finds all possible combinations.

    Time complexity: O(n*m)
    Space complexity: O(n*m)
    """
    comb = []
    for i in range(len(x)):
        for j in range(len(y)):
            comb.append(x[i] + y[j])
    return comb


def find_letter_combinations(digits: str) -> List[str]:
    """
    Finds all possible combinations recursively, by shrinking input digits by 1 element and processing the rest.

    The worst case is 4 letters. So, on each recursion step we'll have x4 more computations to do. Therefore, we have
    exponential complexity.

    For example: input = 234

    loop(234) -> comb(2, loop(34)) -> comb(2, comb(3, loop(4)))
    n_comp:        4*4^2=4^3                         4^2

    Time complexity: O(4^n)
    Space complexity: O(4^n)
    """

    keyboard = {
        "2": ["a", "b", "c"],
        "3": ["d", "e", "f"],
        "4": ["g", "h", "i"],
        "5": ["j", "k", "l"],
        "6": ["m", "n", "o"],
        "7": ["p", "q", "r", "s"],
        "8": ["t", "u", "v"],
        "9": ["w", "x", "y", "z"],
    }

    if len(digits) == 0:
        return []

    def loop(digits: str) -> List[str]:
        if len(digits) == 1:
            return keyboard[digits[0]]
        return find_combinations(keyboard[digits[0]], loop(digits[1:]))

    return loop(digits)


if __name__ == '__main__':
    assert find_letter_combinations("") == []
    assert find_letter_combinations("2") == ["a", "b", "c"]
    assert find_letter_combinations("23") == ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
