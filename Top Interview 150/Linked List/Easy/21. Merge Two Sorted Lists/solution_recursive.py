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


    Time complexity O(n)
    Space complexity O(1)

    """
    if not list1 or not list2:
        return list1 or list2

    if list1.val <= list2.val:
        list1.next = merge_lists(list1.next, list2)
        return list1

    else:
        list2.next = merge_lists(list1, list2.next)
        return list2


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
