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


def add_two_numbers(l1: ListNode, l2: ListNode) -> ListNode:
    """
    In-place approach. We can replace values in existing Lists, instead of defining new List.


    Time Complexity: O(n)
    Space Complexity: O(1)

    """
    head1, head2 = l1, l2  # save link to head nodes
    l1_prev, l2_prev = l1, l2
    carry = 0
    while l1 and l2:
        l1.val += l2.val + carry  # calc sum and replace value in first list
        l1.val, carry = l1.val % 10, l1.val // 10  # consider value that exceeds 10 and update carry
        l2.val = l1.val  # update value in the second list
        l1_prev, l2_prev = l1, l2
        l1, l2 = l1.next, l2.next

    if not l1 and not l2:  # lists have equal length
        if carry > 0:
            l1_prev.next = ListNode(val=carry)  # add node for carry

        return head1

    if l1:  # l1 is longer
        while carry > 0:
            if not l1:  # add node for carry
                l1_prev.next = ListNode(val=carry)
                break
            else:
                l1.val += carry
                l1.val, carry = l1.val % 10, l1.val // 10
                l1_prev = l1
                l1 = l1.next

        return head1

    if l2:  # l2 is longer
        while carry > 0:
            if not l2:  # add node for carry
                l2_prev.next = ListNode(val=carry)
                break
            else:
                l2.val += carry
                l2.val, carry = l2.val % 10, l2.val // 10
                l2_prev = l2
                l2 = l2.next

        return head2


if __name__ == '__main__':
    xs = build_linked_list([2, 4, 3])
    ys = build_linked_list([5, 6, 4])
    actual, expected = add_two_numbers(xs, ys).to_list(), [7, 0, 8]
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    xs = build_linked_list([0])
    ys = build_linked_list([0])
    actual, expected = add_two_numbers(xs, ys).to_list(), [0]
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    xs = build_linked_list([9, 9, 9, 9, 9, 9, 9])
    ys = build_linked_list([9, 9, 9, 9])
    actual, expected = add_two_numbers(xs, ys).to_list(), [8, 9, 9, 9, 0, 0, 0, 1]
    assert actual == expected, f"expected: {expected}, actual: {actual}"
