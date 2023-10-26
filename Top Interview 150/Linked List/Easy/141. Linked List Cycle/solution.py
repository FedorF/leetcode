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
    Let's keep track of nodes that we have already seen. If node/it's id is already in history, then there is a loop.

    Time Complexity: O(N)
    Space Complexity: O(N)
    """
    history = set()
    while head:
        if id(head) in history:
            return True
        else:
            history.add(id(head))
        head = head.next
    return False
