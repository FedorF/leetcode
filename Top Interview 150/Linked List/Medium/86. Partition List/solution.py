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


def partition(head: ListNode, target: int) -> ListNode:
    """
    Keep track on the head of "less" nodes and head of "greater" nodes.
    1. Connect "less" nodes
    2. Connect "greater" nodes
    3. Connect the last "less" node with the head of "greater" nodes.


    Time complexity: O(n)
    Space complexity: O(1)

    """
    if not head:
        return

    head_of_greater = prev_greater = None
    head_of_less = prev_less = None
    cur = head
    while cur:
        if cur.val < target:  # found "less" node
            if prev_greater:  # disconnect last "greater" node
                prev_greater.next = None

            if not head_of_less:
                head_of_less = prev_less = cur
            else:
                prev_less.next = cur  # connect last "less" node with current one

            while cur and cur.val < target:  # iterate through "less" nodes
                prev_less, cur = cur, cur.next

            if not head_of_greater:
                head_of_greater = cur

            prev_less.next = head_of_greater  # link prev_less and "greater" head

        else:  # found "greater" node
            if not head_of_greater:
                head_of_greater = cur

            if prev_greater:  # connect last "greater" node with current one
                prev_greater.next = cur

            prev_greater, cur = cur, cur.next

    if head_of_less:
        return head_of_less

    return head_of_greater


if __name__ == '__main__':
    xs = build_linked_list([1, 4, 3, 2, 5, 2])
    actual, expected = partition(xs, 3).to_list(), [1, 2, 2, 4, 3, 5]
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    xs = build_linked_list([2, 1])
    actual, expected = partition(xs, 2).to_list(), [1, 2]
    assert actual == expected, f"expected: {expected}, actual: {actual}"
