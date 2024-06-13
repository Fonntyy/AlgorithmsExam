# G1: Algo-X returns the number of elements in A that do not have duplicates.
import copy


# G2: Complexity
# Best case: theta(n) - inner loop executes always once when all el. in A are the same
# Worst case: theta(n^2) - inner loop compares to all other el. in A when all el. in A are different

# G3
def better_algo_y(A):
    S = sorted(A)
    n = len(S)
    counter = 0
    for i in range(n):
        if (i == 0 or S[i - 1] != S[i]) and (i == n - 1 or S[i] != S[i + 1]):
            counter += 1
    return counter
