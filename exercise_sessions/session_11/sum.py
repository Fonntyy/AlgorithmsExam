# bottom up - good efficiency
def max_non_adjacent_sum(A):
    n = len(A)
    i = n - 1
    sums_from_i = [None]*n
    while i >= 0:
        sums_from_i[i] = max(
            A[i] + (sums_from_i[i+2] if i+2 < n else 0),
            sums_from_i[i+1] if i+1 < n else 0,
        )
        i -= 1
    return sums_from_i[0]


# top down - bad efficiency
def max_non_adjacent_sum_alt(A):
    return DP(A, 0)


def DP(A, i):
    if i >= len(A):
        return 0
    else:
        return max(
            A[i] + DP(A, i + 2),
            DP(A, i + 1),
        )
