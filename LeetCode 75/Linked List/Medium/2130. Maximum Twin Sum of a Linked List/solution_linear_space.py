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
    Brute-force.


    Time complexity: O(n)
    Space complexity: O(n)

    """
    xs = []
    while head:
        xs.append(head.val)
        head = head.next

    max_sum = 0
    for i in range(len(xs) // 2):
        max_sum = max(max_sum, xs[i] + xs[-1 - i])

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
