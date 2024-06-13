def mountain_sort(A):
    """Implemented using insertion sort. Complexity is therefore theta(n^2)."""
    for i in range(1, len(A)):
        j = i - 1
        while j >= 0 and A[j] > A[j + 1]:
            A[j], A[j + 1] = A[j + 1], A[j]
            j -= 1
    i = len(A) // 2
    j = len(A) - 1
    while i < j:
        A[i], A[j] = A[j], A[i]
        i += 1
        j -= 1
