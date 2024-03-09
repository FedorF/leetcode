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


def rotate_right(head: ListNode, k: int) -> ListNode:
    """

    Time complexity: O(n)
    Space complexity: O(1)

    """
    if not head or k == 0:
        return head

    length = 0
    slow = fast = head
    while fast and fast.next:  # determine list's length
        slow = slow.next
        fast = fast.next.next
        length += 1

    length = 2 * length
    if fast:  # odd number of nodes
        length += 1

    k %= length
    if k == 0:
        return head

    # link the last node with the first one
    if fast:  # odd number of nodes
        fast.next = head
    else:  # even number of nodes
        while slow.next:
            slow = slow.next
        slow.next = head

    # remove k-th link from the end and set up new "head"
    for i in range(length - 1 - k):
        head = head.next
    new_head = head.next
    head.next = None

    return new_head


if __name__ == '__main__':
    xs = build_linked_list([1, 2, 3, 4, 5])
    actual, expected = rotate_right(xs, 2).to_list(), [4, 5, 1, 2, 3]
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    xs = build_linked_list([0, 1, 2])
    actual, expected = rotate_right(xs, 4).to_list(), [2, 0, 1]
    assert actual == expected, f"expected: {expected}, actual: {actual}"
