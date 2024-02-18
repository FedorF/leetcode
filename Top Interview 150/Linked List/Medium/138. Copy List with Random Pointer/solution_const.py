class Node:
    def __init__(self, val=0, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random


def copy_random_list(head: Node) -> Node:
    """

    The main idea is to interweave the nodes of the original and copied lists.
    This interweaving allows us to set the random pointers for the new nodes without additional memory for mapping.


    1) Initialization and Interweaving:
        Traverse the original list. For each node, create a corresponding new node and place it between the current node
        and the current node's next.

    2) Setting Random Pointers:
        Traverse the interweaved list. For each old node, set its corresponding new node's random pointer.

    3) Separating Lists:
        Traverse the interweaved list again to separate the old and new lists.


    Time complexity: O(n)
    Space complexity: O(1)

    """
    if not head:
        return None

    cur = head
    while cur:
        new_node = Node(cur.val, cur.next)
        cur.next = new_node
        cur = new_node.next

    cur = head
    while cur:
        if cur.random:
            cur.next.random = cur.random.next
        cur = cur.next.next

    old_head = head
    new_head = head.next
    curr_old = old_head
    curr_new = new_head

    while curr_old:
        curr_old.next = curr_old.next.next
        curr_new.next = curr_new.next.next if curr_new.next else None
        curr_old = curr_old.next
        curr_new = curr_new.next

    return new_head
