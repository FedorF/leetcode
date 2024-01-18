from typing import List


class StockSpanner:
    """
    Define stack, and keep pairs of price, and it's span: (price, span) in the stack.
    If new price is greater than last price in the stack: pop elements from the stack until, greater price appears.
    Sum spans of excluded items. Append new price and that sum to the stack.

    (See illustration in Readme.md)

    Time complexity: O(len(stack))
    Space complexity: O(len(stack))

    """

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        res = 1  # consider current price
        # compare price with prices in stack
        while self.stack and price >= self.stack[-1][0]:
            _, span = self.stack.pop()
            res += span  # calc total span

        self.stack.append((price, res))  # add a pair of price and total span to stack
        return res


def calc_span(prices: List[int]) -> List[int]:
    """
    Function for testing StockSpanner implementation.


    Time complexity: O(n)
    Space complexity: O(n)

    """
    span_calcer = StockSpanner()
    res = []
    for price in prices:
        res.append(span_calcer.next(price))

    return res


if __name__ == '__main__':
    actual, expected = calc_span([100, 80, 60, 70, 60, 75, 85]), [1, 1, 1, 2, 1, 4, 6]
    assert actual == expected, f"expected: {expected}, actual: {actual}"
