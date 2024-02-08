from typing import List, Optional


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


def reverse(head: Optional[ListNode]) -> Optional[ListNode]:
    """

    Time complexity: O(n)
    Space complexity: O(1)

    """
    if head is None or head.next is None:
        return head

    # init 3 pointers
    prev, cur, next = head, head.next, head.next.next
    # previous node is a tail, so make it point to None
    prev.next = None
    # make current node point to previous node
    cur.next = prev
    while next:
        prev, cur, next = cur, next, next.next
        cur.next = prev

    return cur


def build_linked_list(xs: List[int]) -> ListNode:
    cur_list = ListNode(xs.pop())
    while xs:
        cur_list = ListNode(xs.pop(), cur_list)

    return cur_list


if __name__ == '__main__':
    actual, expected = reverse(build_linked_list([1, 2, 3, 4, 5])).to_list(), [5, 4, 3, 2, 1]
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = reverse(None), None
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = reverse(build_linked_list([1])).to_list(), [1]
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = reverse(build_linked_list([1, 2])).to_list(), [2, 1]
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = reverse(build_linked_list([1, 2, 3])).to_list(), [3, 2, 1]
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = reverse(build_linked_list([1, 2, 3, 4, 5, 6])).to_list(), [6, 5, 4, 3, 2, 1]
    assert actual == expected, f"expected: {expected}, actual: {actual}"
