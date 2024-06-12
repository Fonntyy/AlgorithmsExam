def re_sort(A):
    """Re-sort an array that used to be sorted before some elements were changed to 0."""
    i = 0
    i_sorted = 0
    while i < len(A) and A[i] <= 0:
        if A[i] != 0:
            A[i], A[i_sorted] = A[i_sorted], A[i]
            i_sorted += 1
        i += 1
    j = len(A) - 1
    j_sorted = len(A) - 1
    while j >= 0 and A[j] >= 0:
        if A[j] != 0:
            A[j], A[j_sorted] = A[j_sorted], A[j]
            j_sorted -= 1
        j -= 1
