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


def merge(xs: ListNode, ys: ListNode) -> ListNode:
    """
    Merges 2 sorted list


    Time complexity: O(n)
    Space complexity: O(1)

    """
    if not xs:
        return ys

    if not ys:
        return xs

    if xs.val < ys.val:
        xs.next = merge(xs.next, ys)
        return xs

    ys.next = merge(xs, ys.next)
    return ys


def merge_sorted_linked_lists(lists: List[ListNode]) -> ListNode:
    """
    Brute force solution: merge lists one-by-one.

    Time complexity: O(len(lists) * max(len(lists)))
    Space complexity: O(1)

    """
    if not lists:
        return

    xs = lists.pop()
    while lists:
        xs = merge(xs, lists.pop())

    if not xs:
        return

    return xs


if __name__ == '__main__':
    xs = map(build_linked_list, [[1, 4, 5], [1, 3, 4], [2, 6]])
    actual, expected = merge_sorted_linked_lists(list(xs)).to_list(), [1, 1, 2, 3, 4, 4, 5, 6]
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = merge_sorted_linked_lists([]), None
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = merge_sorted_linked_lists([[]]), None
    assert actual == expected, f"expected: {expected}, actual: {actual}"
