class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def add_two_numbers(l1: ListNode, l2: ListNode) -> ListNode:
    def loop(xs: ListNode, ys: ListNode, val_add: int) -> ListNode:
        if not xs and not ys:
            return ListNode(val_add) if val_add > 0 else None

        elif not xs:
            val_sum = ys.val + val_add
            return ListNode(val_sum % 10, loop(xs, ys.next, val_sum // 10))

        elif not ys:
            val_sum = xs.val + val_add
            return ListNode(val_sum % 10, loop(xs.next, ys, val_sum // 10))

        else:
            val_sum = xs.val + ys.val + val_add
            return ListNode(val_sum % 10, loop(xs.next, ys.next, val_sum // 10))

    return loop(l1, l2, 0)


if __name__ == '__main__':
    pass
    # todo: tests
