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


def move_even_nodes_to_end(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    See Readme.md for the details.

    Time complexity: O(n)
    Space complexity: O(1)

    """
    if head is None or head.next is None:
        return head

    # save evens and odds head nodes
    head_of_odds = odd = head
    head_of_evens = even = head.next

    i = 3
    head = head.next.next
    while head:
        if i % 2 == 0:
            even.next = head
            even = even.next
        else:
            odd.next = head
            odd = odd.next

        head = head.next
        i += 1

    # Make the last "odd" node point to "head" of evens
    odd.next = head_of_evens
    # Make the last "even" node point to None
    even.next = None
    return head_of_odds


def build_linked_list(xs: List[int]) -> ListNode:
    cur_list = ListNode(xs.pop())
    while xs:
        cur_list = ListNode(xs.pop(), cur_list)

    return cur_list


if __name__ == '__main__':
    actual, expected = move_even_nodes_to_end(None), None
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = move_even_nodes_to_end(build_linked_list([1])).to_list(), [1]
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = move_even_nodes_to_end(build_linked_list([1, 2])).to_list(), [1, 2]
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = move_even_nodes_to_end(build_linked_list([1, 2, 3])).to_list(), [1, 3, 2]
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = move_even_nodes_to_end(build_linked_list([1, 2, 3, 4, 5])).to_list(), [1, 3, 5, 2, 4]
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = move_even_nodes_to_end(build_linked_list([2, 1, 3, 5, 6, 4, 7])).to_list(), [2, 3, 6, 7, 1, 5, 4]
    assert actual == expected, f"expected: {expected}, actual: {actual}"
