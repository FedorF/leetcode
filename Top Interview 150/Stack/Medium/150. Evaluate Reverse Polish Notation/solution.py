from typing import List


def eval_polish_notation(tokens: List[str]) -> int:
    """
    Use stack for keeping numbers and perform calculation when operation token appears.

    Time complexity: O(n)
    Space complexity: O(1)
    """
    operations = {'+', '-', '*', '/'}
    stack = []
    for token in tokens:
        if token in operations:
            y, x = stack.pop(), stack.pop()
            result = eval(f"{x}{token}{y}")
            stack.append(int(result))
        else:
            stack.append(token)
    return int(stack[0])


if __name__ == '__main__':
    assert eval_polish_notation(["2", "1", "+", "3", "*"]) == 9
    assert eval_polish_notation(["4", "13", "5", "/", "+"]) == 6
    assert eval_polish_notation(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]) == 22
