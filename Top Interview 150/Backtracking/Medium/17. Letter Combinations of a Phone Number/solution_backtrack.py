from typing import List


def find_letter_combinations(digits: str) -> List[str]:
    """
    Time complexity: O(4^n)
    Space complexity: O(4^n)

    """
    if len(digits) == 0:
        return []

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

    def backtrack(ind: int = 0, comb: str = ""):
        if ind == len(digits):
            res.append(comb)
            return

        for letter in keyboard[digits[ind]]:
            backtrack(ind + 1, comb + letter)

    res = []
    backtrack()
    return res


if __name__ == '__main__':
    assert find_letter_combinations("") == []
    assert find_letter_combinations("2") == ["a", "b", "c"]
    assert find_letter_combinations("23") == ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
