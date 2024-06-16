# G1: Algo-X returns the maximal length of any contiguous subsequence of A
# whose total value is equal to an element of B. If no such sequence exists,
# the result is 0.
# The complexity is theta(n^4)

# G2
def better_algo_x(A, B):
    """Complexity theta(n^3)."""
    for l in range(len(A), 0, -1):
        for j in range(len(B)):
            s = 0
            for k in range(l):
                s += A[k]
            if s == B[j]:
                return l
            for i in range(1, len(A) - l + 1):
                s = s - A[i - 1] + A[i + l - 1]
                if s == B[j]:
                    return l
    return 0
