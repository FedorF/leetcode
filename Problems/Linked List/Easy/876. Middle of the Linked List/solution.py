from typing import Optional


class ListNode:
    def __init__(self, val=0, _next=None):
        self.val = val
        self.next = _next


def find_middle_node(head: Optional[ListNode]) -> Optional[ListNode]:
    if head is None:
        return None

    cur_node = head
    nodes = []
    cnt_nodes = 0
    while cur_node:
        cnt_nodes += 1.
        nodes.append(cur_node)
        cur_node = cur_node.next

    return nodes[cnt_nodes // 2]


if __name__ == '__main__':
    actual = find_middle_node(ListNode(_next=ListNode(val=1, _next=ListNode(val=2, _next=None)))).val
    expected = 1
    assert actual == expected, f"expected: {expected}, actual: {actual}"
    assert find_middle_node(ListNode(_next=None)).val == 0
    assert find_middle_node(ListNode(_next=ListNode(val=1, _next=None))).val == 1
