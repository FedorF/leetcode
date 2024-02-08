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


def delete_mid_node(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    Make one pass to calculate number of elements.
    Make second pass to build list with no middle element.

    Time complexity: O(n)
    Space complexity: O(n)

    """
    xs = []
    while head:
        xs.append(head.val)
        head = head.next

    if len(xs) == 1:
        return

    i, mid = len(xs) - 1, len(xs) // 2
    node = None
    while xs:
        if i == mid:
            xs.pop()
        else:
            node = ListNode(xs.pop(), node)
        i -= 1

    return node


def build_linked_list(xs: List[int]) -> ListNode:
    cur_list = ListNode(xs.pop())
    while xs:
        cur_list = ListNode(xs.pop(), cur_list)

    return cur_list


if __name__ == '__main__':
    actual, expected = delete_mid_node(build_linked_list([1, 3, 4, 7, 1, 2, 6])).to_list(), [1, 3, 4, 1, 2, 6]
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = delete_mid_node(build_linked_list([1, 2, 3, 4])).to_list(), [1, 2, 4]
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = delete_mid_node(build_linked_list([2, 1])).to_list(), [2]
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = delete_mid_node(build_linked_list([1])), None
    assert actual == expected, f"expected: {expected}, actual: {actual}"
