from typing import List


def generate_parentheses(k: int) -> List[str]:
    """
    Same approach, but use string instead of list, so we can save some time complexity by not coping elements in the
    good case.

    Time complexity: O(2^k) ???
    Space complexity: O(k)
    """
    res = []

    def backtrack(s: str = "", cnt_open: int = 0, cnt_close: int = 0):
        if (cnt_open > k) or (cnt_close > k) or (cnt_open < cnt_close):
            return

        if (len(s) == k * 2) and (cnt_open == cnt_close):
            res.append(s)

        backtrack(s + "(", cnt_open + 1, cnt_close)  # run left branch
        backtrack(s + ")", cnt_open, cnt_close + 1)  # run right branch

    backtrack()
    return res


if __name__ == '__main__':
    assert generate_parentheses(1) == ["()"]
    assert generate_parentheses(3) == ["((()))", "(()())", "(())()", "()(())", "()()()"]
