class List:
    def __init__(self, v):
        self.value = v
        self.next = None

# ------- UTILITY ----------


def print_list(l):
    while l is not None:
        print(l.value)
        l = l.next


def list_of(lst):
    """Make a singly linked list out of a python list."""
    if lst == []:
        return None
    linked_list = List(lst[0])
    pointer = linked_list
    i = 1
    while i < len(lst):
        pointer.next = List(lst[i])
        pointer = pointer.next
        i += 1
    return linked_list


# ------- EXERCISES ----------


def reverse_list(l):
    """Inverses List l in place."""
    if l is None or l.next is None:
        # trivially reversed
        return l
    else:
        # KNOW: l has at least 2 elements
        l.value, l.next.value = l.next.value, l.value
        rest = l.next.next
        l.next.next = None
        # l is now a list of the first two elements of original l, in reverse order
        # rest is the original l without the first two elements
        rest_reversed = reverse_list(rest)
        return concatenate_lists(rest_reversed, l)

# COMPLEXITY: theta(n^2)


def concatenate_lists(first_list, second_list):
    """Concatenate two lists in place."""
    if first_list is None:
        return second_list
    # Know: first_list has at least one element
    pointer = first_list
    while pointer.next is not None:
        pointer = pointer.next
    # Know: pointer.next is None
    pointer.next = second_list
    return first_list

# COMPLEXITY
# Worst case: theta(n)
# Best case: 0(1)


