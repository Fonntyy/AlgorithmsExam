# G1: Algo-X returns the length of the longest contiguous subarray where at each index i, A[i] > B[i]
# Complexity is theta(n^2) in the worst case (A[i] > B[i] for all i)
# and theta(n) in the best case (A[i] < B[i] for all i)

# G2:
def better_algo_x(A, B):
    i = 0
    j = 0
    best_length = 0
    while j < len(A):
        if A[j] > B[j]:
            curr_length = j - i + 1
            if curr_length > best_length:
                best_length = curr_length
            j = j + 1
        else:
            i = j = j + 1
    return best_length
