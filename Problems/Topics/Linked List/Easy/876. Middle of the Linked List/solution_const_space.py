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


def find_mid_node(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    Two pointers:
    1) Slow
    2) Fast

    The fast moves 2 times faster than the slow one. So, when fast reach the end, slow would be the middle node


    Time complexity: O(n)
    Space complexity: O(1)

    """
    slow = fast = head
    while fast and fast.next:
        slow, fast = slow.next, fast.next.next

    return slow


def build_linked_list(xs: List[int]) -> ListNode:
    cur_list = ListNode(xs.pop())
    while xs:
        cur_list = ListNode(xs.pop(), cur_list)

    return cur_list


if __name__ == '__main__':
    actual, expected = find_mid_node(build_linked_list([1, 2, 3, 4, 5, 6])).to_list(), [4, 5, 6]
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = find_mid_node(build_linked_list([1, 2, 3, 4, 5])).to_list(), [3, 4, 5]
    assert actual == expected, f"expected: {expected}, actual: {actual}"
