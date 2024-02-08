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


def calc_max_mirror_pair_sum(head: Optional[ListNode]) -> int:
    """
    1. Find middle node
    2. Reverse second half of list

    (See Readme.md)


    Time complexity: O(n)
    Space complexity: O(1)

    """
    # let's find middle node
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # now "slow" - is a head node of second half
    # let's reverse second half
    prev, cur = None, slow
    while cur:
        next = cur.next
        cur.next = prev
        prev = cur
        cur = next

    # now "prev" - is a head node of reversed second half
    # let's iterate through both half simultaneously and calculate paired sum
    max_sum = 0
    while prev:
        max_sum = max(max_sum, head.val + prev.val)
        head = head.next
        prev = prev.next

    return max_sum


def build_linked_list(xs: List[int]) -> ListNode:
    cur_list = ListNode(xs.pop())
    while xs:
        cur_list = ListNode(xs.pop(), cur_list)

    return cur_list


if __name__ == '__main__':
    actual, expected = calc_max_mirror_pair_sum(build_linked_list([1, 2, 50, 50, 2, 1])), 100
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = calc_max_mirror_pair_sum(build_linked_list([1, 50, 2, 2, 50, 1])), 100
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = calc_max_mirror_pair_sum(build_linked_list([50, 1, 2, 2, 1, 50])), 100
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = calc_max_mirror_pair_sum(build_linked_list([5, 4, 2, 1])), 6
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = calc_max_mirror_pair_sum(build_linked_list([4, 2, 2, 3])), 7
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = calc_max_mirror_pair_sum(build_linked_list([1, 100000])), 100001
    assert actual == expected, f"expected: {expected}, actual: {actual}"
