class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


def print_list(L):
    """Prints a singly-linked list."""
    current = L
    while current:
        print(current.value, end=" -> ")
        current = current.next
    print("\n")


def merge_two_sorted_lists(L1, L2):
    """Merge two singly-linked lists that are in non-decreasing order.
    Works in place.
    """
    # BASE CASE (trivial sort)
    if L1 is None:
        return L2
    if L2 is None:
        return L1

    # RECURSIVE CASE
    if L1.value < L2.value:
        L1.next = merge_two_sorted_lists(L1.next, L2)
        return L1
    else:
        # KNOW: L2.value <= L1.value
        L2.next = merge_two_sorted_lists(L1, L2.next)
        return L2
