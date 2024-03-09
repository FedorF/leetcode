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


def merge_sorted_linked_lists(lists: List[ListNode]) -> ListNode:
    """
    Split lists into parts and merge


    Time complexity: O(max(len(lists)) * log(len(lists)))
    Space complexity: O(1)

    """
    if not lists:
        return

    def merge_two_lists(xs: ListNode, ys: ListNode) -> ListNode:
        """
        Merge 2 sorted list

        Time complexity: O(n)
        Space complexity: O(1)

        """
        if not xs:
            return ys

        if not ys:
            return xs

        if xs.val < ys.val:
            xs.next = merge_two_lists(xs.next, ys)
            return xs

        ys.next = merge_two_lists(xs, ys.next)
        return ys

    def split_and_merge(left: int = 0, right: int = len(lists) - 1) -> ListNode:
        """
        Split and merges.
        Keeps two pointers: starting and ending position of input list


        Time complexity: O(log(n) * n)
        Space complexity: O(1)

        """
        if left == right:
            return lists[left]

        if right - left == 1:
            return merge_two_lists(lists[left], lists[right])

        mid = left + (right - left) // 2
        return merge_two_lists(split_and_merge(left, mid), split_and_merge(mid + 1, right))

    res = split_and_merge()
    if not res:
        return

    return res


if __name__ == '__main__':
    xs = map(build_linked_list, [[1, 4, 5], [1, 3, 4], [2, 6]])
    actual, expected = merge_sorted_linked_lists(list(xs)).to_list(), [1, 1, 2, 3, 4, 4, 5, 6]
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = merge_sorted_linked_lists([]), None
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = merge_sorted_linked_lists([[]]), None
    assert actual == expected, f"expected: {expected}, actual: {actual}"
