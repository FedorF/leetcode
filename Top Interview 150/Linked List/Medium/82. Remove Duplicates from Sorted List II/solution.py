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


def remove_duplicates(head: ListNode) -> ListNode:
    """

    Time complexity: O(n)
    Space complexity: O(1)

    """
    prev, cur = None, head
    while cur:
        if cur.next and cur.val == cur.next.val:  # found duplicate
            duplicate = cur.val
            while cur and cur.val == duplicate:  # skip duplicated nodes
                cur = cur.next

            if not cur:  # duplicated nodes were at the end of the list
                if not prev:  # no nodes left in list
                    return
                prev.next = None
        else:
            if not prev:  # duplicated nodes were at the beginning of the list
                head = cur
            else:
                prev.next = cur
            prev, cur = cur, cur.next

    return head


if __name__ == '__main__':
    xs = build_linked_list([1, 2, 3, 3, 4, 4, 5])
    actual, expected = remove_duplicates(xs).to_list(), [1, 2, 5]
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    xs = build_linked_list([1, 1, 1, 2, 3])
    actual, expected = remove_duplicates(xs).to_list(), [2, 3]
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    xs = build_linked_list([1, 2, 2, 2, 2])
    actual, expected = remove_duplicates(xs).to_list(), [1]
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    xs = build_linked_list([1, 1, 1, 2, 2, 2, 2])
    actual, expected = remove_duplicates(xs), None
    assert actual == expected, f"expected: {expected}, actual: {actual}"
