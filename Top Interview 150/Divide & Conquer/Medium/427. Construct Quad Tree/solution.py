from typing import List, Optional


class Node:
    def __init__(
            self,
            val: float,
            is_leaf: int,
            top_left: Optional[int] = None,
            top_right: Optional[int] = None,
            bottom_left: Optional[int] = None,
            bottom_right: Optional[int] = None,
    ):
        self.val = val
        self.is_leaf = is_leaf
        self.top_left = top_left
        self.top_right = top_right
        self.bottom_left = bottom_left
        self.bottom_right = bottom_right


def construct(grid: List[List[int]]) -> Node:
    def build(row_st: int, row_end: int, col_st: int, col_end: int) -> Node:
        if row_st == row_end or col_st == col_end:
            return Node(grid[row_st][col_st], 1)

        row_mid = row_st + (row_end - row_st) // 2
        col_mid = col_st + (col_end - col_st) // 2

        top_left = build(row_st, row_mid, col_st, col_mid)
        top_right = build(row_st, row_mid, col_mid + 1, col_end)
        bottom_left = build(row_mid + 1, row_end, col_st, col_mid)
        bottom_right = build(row_mid + 1, row_end, col_mid + 1, col_end)

        children_sum = top_left.val + top_right.val + bottom_left.val + bottom_right.val
        if children_sum == 4:
            return Node(1, 1)

        if children_sum == 0:
            return Node(0, 1)

        return Node(children_sum / 4, 0, top_left, top_right, bottom_left, bottom_right)

    return build(0, len(grid) - 1, 0, len(grid) - 1)
