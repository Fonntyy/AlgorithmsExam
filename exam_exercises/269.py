def e_top_sort(A):
    """Sorts an array A in e-top order with an average-case time complexity of theta(n)."""
    n = len(A)

    # k is the median of elements in A
    k = selection(A, n//2 if n % 2 == 0 else (n + 1)//2)

    i = 1  # even element
    j = 0  # odd element
    while i < n or j < n:
        if i < n and A[i] <= k:
            i += 2
        elif j < n and k <= A[j]:
            j += 2
        else:
            if i < n and j < n:
                # KNOW: A[i] > A[j]
                A[i], A[j] = A[j], A[i]
            i += 2
            j += 2


def selection(A, k):
    """Select the kth smallest (0-based) element in A."""
    n = len(A)

    pivot = A[0]
    smaller = []
    equal = [A[0]]
    greater = []

    for i in range(n):
        if A[i] < pivot:
            smaller.append(A[i])
        elif A[i] > pivot:
            greater.append(A[i])
        else:
            equal.append(A[i])

    if k < len(smaller):
        return selection(smaller, k)
    # KNOW: len(smaller) <= k
    elif k < len(smaller) + len(equal):
        return pivot
    else:
        return selection(greater, k - len(smaller) - len(equal))
