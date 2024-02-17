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


def remove_node(head: ListNode, n: int) -> ListNode:
    """

    Time complexity: O(n)
    Space complexity: O(1)

    """
    length = -1
    cur = ListNode(-1, head)
    while cur:
        length += 1
        cur = cur.next

    if length - n == 0:
        return head.next

    cur = ListNode(-1, head)
    for i in range(length - n):
        cur = cur.next

    cur.next = cur.next.next
    return head


if __name__ == '__main__':
    xs = build_linked_list([1, 2, 3, 4, 5])
    actual, expected = remove_node(xs, 2).to_list(), [1, 2, 3, 5]
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    xs = build_linked_list([1])
    actual, expected = remove_node(xs, 1), None
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    xs = build_linked_list([1, 2])
    actual, expected = remove_node(xs, 1).to_list(), [1]
    assert actual == expected, f"expected: {expected}, actual: {actual}"
