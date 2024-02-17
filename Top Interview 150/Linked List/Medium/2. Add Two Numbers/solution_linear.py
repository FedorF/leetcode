from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        self.repr = []

    def to_list(self):
        if self.repr:
            return self.repr

        cur = self
        while cur:
            self.repr.append(cur.val)
            cur = cur.next

        return self.repr

    def __repr__(self):
        """
        Function for representation.

        """
        if self.repr:
            return str(self.repr)

        cur = self
        while cur:
            self.repr.append(cur.val)
            cur = cur.next
        return str(self.repr)


def build_linked_list(xs: List[int]) -> ListNode:
    cur_list = ListNode(xs.pop())
    while xs:
        cur_list = ListNode(xs.pop(), cur_list)

    return cur_list


def add_two_numbers(xs: ListNode, ys: ListNode) -> ListNode:
    """

    Time Complexity: O(n)
    Space Complexity: O(n)

    """

    def dfs(l1: ListNode, l2: ListNode, val_add: int = 0) -> ListNode:
        if not l1 and not l2:
            return ListNode(val_add) if val_add > 0 else None

        elif not l1:
            val_sum = l2.val + val_add
            return ListNode(val_sum % 10, dfs(l1, l2.next, val_sum // 10))

        elif not l2:
            val_sum = l1.val + val_add
            return ListNode(val_sum % 10, dfs(l1.next, l2, val_sum // 10))

        else:
            val_sum = l1.val + l2.val + val_add
            return ListNode(val_sum % 10, dfs(l1.next, l2.next, val_sum // 10))

    return dfs(xs, ys)


if __name__ == '__main__':
    xs = build_linked_list([2, 4, 3])
    ys = build_linked_list([5, 6, 4])
    actual, expected = add_two_numbers(xs, ys).to_list(), [7, 0, 8]
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    xs = build_linked_list([0])
    ys = build_linked_list([0])
    actual, expected = add_two_numbers(xs, ys).to_list(), [0]
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    xs = build_linked_list([9, 9, 9, 9, 9, 9, 9])
    ys = build_linked_list([9, 9, 9, 9])
    actual, expected = add_two_numbers(xs, ys).to_list(), [8, 9, 9, 9, 0, 0, 0, 1]
    assert actual == expected, f"expected: {expected}, actual: {actual}"
