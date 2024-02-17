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
    One pass approach.
    1) Use slow and fast pointers to determine List length. Slow pointer would point on middle node.
    2) If n > mid_node, continue running forward until reach (n-1)th node.
       If n <= mid_node, start iterating from the head until reach (n-1)th node.
    3) Remove n-th node


    Time complexity: O(n)
    Space complexity: O(1)

    """
    slow, fast = head, head
    n_nodes = 0
    # determine length of List
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        n_nodes += 1

    n_nodes *= 2
    if fast:  # odd number of nodes
        n_nodes += 1

    ind_to_del = n_nodes - n

    if ind_to_del == 0:  # we should remove head node
        head = head.next
        return head

    if ind_to_del <= n_nodes // 2:  # start from the head node
        slow = head
        i = 0
    else:  # continue iteration from middle node
        i = n_nodes // 2

    while i < ind_to_del - 1:  # reach (n-1)th node
        slow = slow.next
        i += 1

    slow.next = slow.next.next  # remove n-th node
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
