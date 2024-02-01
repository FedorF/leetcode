class MinStack:
    """
    Store value and current minimum element.

    Time complexity: O(1)
    Space complexity: O(N)

    """

    def __init__(self):
        self.stack = []

    def push(self, val: int):
        if self.stack:
            _, min_el = self.stack[-1]  # compare previous minimum value with new val
            self.stack.append((val, min(val, min_el)))
        else:
            self.stack.append((val, val))

    def pop(self):
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]


def run_test(commands, xs):
    """
    Function for testing MinStack implementation.

    """
    min_stack = MinStack()
    res = []
    for i in range(len(commands)):
        if xs[i]:
            res.append(getattr(min_stack, commands[i])(xs[i][0]))
        else:
            res.append(getattr(min_stack, commands[i])())
    return res


if __name__ == '__main__':
    actual = run_test(["push", "push", "push", "getMin", "pop", "top", "getMin"],
                      [[-2], [0], [-3], [], [], [], []])
    expected = [None, None, None, -3, None, 0, -2]
    assert actual == expected, f"expected: {expected}, actual: {actual}"
