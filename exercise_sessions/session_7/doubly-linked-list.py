class List:
    def __init__(self):
        self.value = None
        self.next = self
        self.prev = self


def list_append (l, v):
    """Put value v into a new node at the end of the list l.
    l is a reference to the sentinel.
    """
    n = List()
    n.value = v
    n.prev = l.prev
    n.next = l
    n.prev.next = n
    n.next.prev = n


def print_list(sentinel):
    l = sentinel.next
    while l != sentinel:
        print(l.value)
        l = l.next


# ------- UTILITY ----------


def list_of(lst):
    """Make a doubly linked list out of a python list."""
    if lst == []:
        return None
    linked_list = List()
    for el in lst:
        list_append(linked_list, el)
    return linked_list


# -------- EXERCISES ----------


def reverse_list(l):
    """Inverses List l in place."""
    if l.next is l or l.next.next is l:
        # trivial reverse - l has 0 or 1 element
        return l

    # KNOW: len(l) >= 2

    # reverse sentinel.next and sentinel.prev
    sentinel = l
    sentinel.next, sentinel.prev = sentinel.prev, sentinel.next

    # reverse l.next and l.prev for all elements
    l = l.next
    while l is not sentinel:
        l.next, l.prev = l.prev, l.next
        l = l.next
    return sentinel


def concatenate_lists(l1,l2):
    """Concatenate two lists in place."""
    if l1.next is l1:
        return l2
    if l2.next is l2:
        return l1
    # Know: both l1 and l1 have at least one element

    # strategy: eliminate sentinel of l2

    sentinel = l1
    last_l1 = l1.prev
    first_l2 = l2.next
    last_l2 = l2.prev

    # connect the last element of l1 to the first element of l2
    last_l1.next = first_l2
    first_l2.prev = last_l1

    # connect the last element of l2 to the sentinel
    last_l2.next = sentinel
    sentinel.prev = last_l2

    # return the only sentinel left
    return sentinel


# COMPLEXITY: O(1)
