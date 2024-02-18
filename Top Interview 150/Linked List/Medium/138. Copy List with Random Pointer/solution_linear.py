class Node:
    def __init__(self, val=0, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random


def copy_random_list(head: Node) -> Node:
    """

    Time complexity: O(n)
    Space complexity: O(n)

    """
    if not head:
        return None

    new_ind_to_node = {}  # map index to corresponding node in new List
    ind_to_random = {}  # map index to corresponding random node id in original List
    id_to_ind = {}  # map node id to corresponding index in original List

    new_head = new_prev = Node(0)  # fake head node in new List
    cur = head
    i = 0
    # traverse through original List and create nodes of new List
    while cur:
        new_prev.next = Node(cur.val)
        new_prev = new_prev.next
        new_ind_to_node[i] = new_prev
        if cur.random is None:
            ind_to_random[i] = None
        else:
            ind_to_random[i] = id(cur.random)

        id_to_ind[id(cur)] = i

        cur = cur.next
        i += 1

    new_head = new_head.next  # delete fake head node

    cur = new_head
    i = 0
    # traverse through new List and fill random links
    while cur:
        if ind_to_random[i] is None:
            cur.random = None
        else:
            random_ind = id_to_ind[ind_to_random[i]]
            cur.random = new_ind_to_node[random_ind]
        cur = cur.next
        i += 1

    return new_head
