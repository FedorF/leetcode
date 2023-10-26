from typing import List, Optional


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


def build_list_node(nodes: List[float]) -> Optional[ListNode]:
    if len(nodes) == 0:
        return None

    def build_node(i: int = 0) -> Optional[ListNode]:
        if i < len(nodes):
            return ListNode(nodes[i], build_node(i + 1))
        else:
            return None

    return build_node()


def merge_lists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    """
    Let's define a new ListNode and fill it sequentially in recursive loop.

    Time complexity O(m+n)
    Space complexity O(m+n)
    """
    merged = None
    if list1 and list2:
        if list1.val < list2.val:
            if merged:
                merged.val = list1.val
            else:
                merged = ListNode(list1.val)
            merged.next = merge_lists(list1.next, list2)
        else:
            if merged:
                merged.val = list2.val
            else:
                merged = ListNode(list2.val)
            merged.next = merge_lists(list2.next, list1)
    elif list1:
        if merged:
            merged.val = list1.val
        else:
            merged = ListNode(list1.val)
        merged.next = list1.next
    elif list2:
        if merged:
            merged.val = list2.val
        else:
            merged = ListNode(list2.val)
        merged.next = list2.next
    return merged


if __name__ == '__main__':
    list1 = build_list_node([1, 2, 4])
    list2 = build_list_node([1, 3, 4])
    actual = merge_lists(list1, list2)
    expected = [1, 1, 2, 3, 4, 4]
    assert actual.to_list() == expected

    list1 = build_list_node([])
    list2 = build_list_node([0])
    actual = merge_lists(list1, list2)
    expected = [0]
    assert actual.to_list() == expected
