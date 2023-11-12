from typing import Optional


class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next

    def to_list(self):
        out = []
        node = self
        while node:
            out.append(node.val)
            node = node.next
        return out

    def __repr__(self):
        return '->'.join(str(x) for x in self.to_list())


def has_cycle(head: Optional[ListNode]) -> bool:
    """
    Turtle and rabbit approach: define two pointers slow and fast.
    If there is a loop, pointers would meet each other at some point.

    Time Complexity: O(N)
    Space Complexity: O(1)
    """
    if not head:
        return False

    slow, fast = head, head.next
    while fast:
        if slow is fast:
            return True

        if not fast.next:
            return False

        slow = slow.next
        fast = fast.next.next

    return False
