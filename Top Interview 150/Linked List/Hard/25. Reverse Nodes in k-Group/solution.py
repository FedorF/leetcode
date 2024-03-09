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


def length_linked_list(head: ListNode) -> int:
    """


    Time complexity: O(n)
    Space complexity: O(1)

    """
    n_nodes = 0
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        n_nodes += 1

    n_nodes *= 2
    if fast:  # odd number of nodes
        n_nodes += 1

    return n_nodes


def reverse_k_groups(head: ListNode, k: int) -> ListNode:
    """

    Time complexity: O(n)
    Space complexity: O(1)

    """
    if not head or not head.next:
        return head

    if k > length_linked_list(head):  # not enough nodes to make a group
        return head

    prev, curr = None, head
    for _ in range(k):  # reverse current group
        next_node = curr.next
        curr.next = prev
        prev, curr = curr, next_node

    # now "prev" points to current group's head
    # "head" points to current group's tail
    # "curr" points to the head of a following group
    head.next = reverse_k_groups(curr, k)
    return prev


if __name__ == '__main__':
    xs = build_linked_list([1, 2])
    actual, expected = reverse_k_groups(xs, 2).to_list(), [2, 1]
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    xs = build_linked_list([1, 2, 3, 4, 5])
    actual, expected = reverse_k_groups(xs, 2).to_list(), [2, 1, 4, 3, 5]
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    xs = build_linked_list([1, 2, 3, 4, 5])
    actual, expected = reverse_k_groups(xs, 3).to_list(), [3, 2, 1, 4, 5]
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    xs = build_linked_list([1, 2, 3, 4, 5])
    actual, expected = reverse_k_groups(xs, 5).to_list(), [5, 4, 3, 2, 1]
    assert actual == expected, f"expected: {expected}, actual: {actual}"
