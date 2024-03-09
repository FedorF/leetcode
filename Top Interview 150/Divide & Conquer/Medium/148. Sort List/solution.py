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


def find_mid_node(head: ListNode) -> ListNode:
    """
    Returns list's middle node

    For example,
    build_linked_list([1, 2, 3, 4, 5])  ->  3
    build_linked_list([1, 2, 3, 4, 5, 6])  ->  3


    Time complexity: O(n)
    Space complexity: O(1)

    """
    if not head:
        return

    slow, fast = head, head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow


def merge_sorted_linked_lists(xs: ListNode, ys: ListNode) -> ListNode:
    """
    Returns merged sorted list


    Time complexity: O(n)
    Space complexity: O(1)

    """
    if not xs:
        return ys

    if not ys:
        return xs

    if xs.val < ys.val:
        xs.next = merge_sorted_linked_lists(xs.next, ys)
        return xs

    ys.next = merge_sorted_linked_lists(xs, ys.next)
    return ys


def sort_linked_list(head: ListNode) -> ListNode:
    """
    Merge sort approach (see Readme.md).

    1. Split list by half
          ...
    2. Merge two halfs keeping ascending order.


    Time complexity: O(n*log(n))
    Space complexity: O(1)

    """
    if not head or not head.next:
        return head

    mid_node = find_mid_node(head)
    right_head = mid_node.next
    mid_node.next = None

    left_sorted = sort_linked_list(head)
    right_sorted = sort_linked_list(right_head)
    return merge_sorted_linked_lists(left_sorted, right_sorted)


if __name__ == '__main__':
    xs = build_linked_list([4, 2, 1, 3])
    actual, expected = sort_linked_list(xs).to_list(), [1, 2, 3, 4]
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    xs = build_linked_list([-1, 5, 3, 4, 0])
    actual, expected = sort_linked_list(xs).to_list(), [-1, 0, 3, 4, 5]
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = sort_linked_list(None), None
    assert actual == expected, f"expected: {expected}, actual: {actual}"
