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


def merge_lists(xs: Optional[ListNode], ys: Optional[ListNode]) -> Optional[ListNode]:
    """


    Time complexity O(n)
    Space complexity O(1)

    """
    if not xs:
        return ys

    if not ys:
        return xs

    if xs.val < ys.val:
        head = prev = xs
        xs = xs.next
    else:
        head = prev = ys
        ys = ys.next

    while xs or ys:
        if not xs:
            prev.next = ys
            ys = ys.next

        elif not ys:
            prev.next = xs
            xs = xs.next

        elif xs.val < ys.val:
            prev.next = xs
            xs = xs.next

        else:
            prev.next = ys
            ys = ys.next

        prev = prev.next

    return head


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
