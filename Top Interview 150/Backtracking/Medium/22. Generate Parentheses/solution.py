from typing import List


def generate_parentheses(k: int) -> List[str]:
    """
    Keep track on how many opening and closing parentheses we currently have. The idea is to append ( for the left
    branch and ) for  the  right. If closing counter is greater than opening then backtrack.
    We append a combination to result if counters are equals, and we have reached necessary length.

    Time complexity: O(k*2^k) ???
    Space complexity: O(k)
    """
    res = []

    def backtrack(comb: List[str], cnt_open: int = 0, cnt_close: int = 0):
        if (cnt_open > k) or (cnt_close > k) or (cnt_open < cnt_close):
            return
        if (len(comb) == k * 2) and (cnt_open == cnt_close):
            res.append("".join(comb))

        comb.append("(")
        backtrack(comb, cnt_open + 1, cnt_close)  # run left branch
        comb.pop()
        comb.append(")")
        backtrack(comb, cnt_open, cnt_close + 1)  # run right branch
        comb.pop()

    backtrack([])
    return res


if __name__ == '__main__':
    assert generate_parentheses(1) == ["()"]
    assert generate_parentheses(3) == ["((()))", "(()())", "(())()", "()(())", "()()()"]
