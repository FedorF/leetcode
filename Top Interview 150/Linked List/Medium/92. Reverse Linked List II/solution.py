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


def reverse_between(head: ListNode, left: int, right: int) -> ListNode:
    """
    Approach:
    1. "Prior" node (before "left" node) should point to "right" node.
    2. "Left" node should point to following "right" node.
    3. Nodes between "left" and "right" should be reversed

    (see Readme.md)

    Time complexity: O(n)
    Space complexity: O(1)

    """
    if (not head.next) or (left == right):  # single node in list, or no change
        return head

    prior, left_node = None, head
    for i in range(left - 1):  # let's find "left" and "prior" to it nodes
        prior, left_node = left_node, left_node.next

    prev, cur = left_node, left_node.next
    for i in range(right - left):  # let's reverse nodes between
        next_node = cur.next
        cur.next = prev
        prev, cur = cur, next_node

    left_node.next = cur  # make "left" node point to following node
    if not prior:  # reverse starts with head node; so replace head node with "right" one
        head = prev
    else:
        prior.next = prev  # make "prior" node point to "right" one

    return head


if __name__ == '__main__':
    xs = build_linked_list([1, 2, 3, 4, 5])
    actual, expected = reverse_between(xs, left=1, right=5).to_list(), [5, 4, 3, 2, 1]
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    xs = build_linked_list([1, 2, 3, 4, 5])
    actual, expected = reverse_between(xs, left=1, right=4).to_list(), [4, 3, 2, 1, 5]
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    xs = build_linked_list([1, 2, 3, 4, 5])
    actual, expected = reverse_between(xs, left=2, right=4).to_list(), [1, 4, 3, 2, 5]
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    xs = build_linked_list([5])
    actual, expected = reverse_between(xs, left=1, right=1).to_list(), [5]
    assert actual == expected, f"expected: {expected}, actual: {actual}"
