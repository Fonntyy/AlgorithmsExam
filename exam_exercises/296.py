def minimal_k_interval_cover_length(A, k):
    """We want to cover a set of n numbers in A with a set of k intervals such that the total
    length of the intervals is minimal. minimal_k_interval_cover_length returns the minimal
    length of these intervals.
    """
    n = len(A)
    B = sorted(A)  # merge sort into non-decreasing order - complexity O(n * log n)
    total_length = B[n - 1] - B[0]

    gabs = []
    for i in range(1, n):  # complexity O(n)
        gabs.append(B[i] - B[i - 1])
    gabs_sorted = sorted(gabs, reverse=True)  # merge sort into non-increasing order - complexity O(n * log n)
    # LARGEST gab is the FIRST element in gabs_sorted
    # SECOND-LARGEST gab is the SECOND element in gabs_sorted
    # etc.

    # to create k intervals there needs to be k-1 gabs
    # if k is larger than n, we subtract all gabs so total_length is 0
    gabs_length = 0
    for i in range( min(k - 1, n) ):  # complexity O(n)
        gabs_length += gabs_sorted[i]

    return total_length - gabs_length

# COMPLEXITY: O(n * log n) - that of a sorting algorithm


