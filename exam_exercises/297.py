# Algo-X returns the sum of the k smallest values in A.
# If A contains less than k values, then the result is nil.
# The complexity is Θ(n^2), since there are two nested loops
# that are run without shortcuts in the worst case of k > n.

# STRATEGY:
# It is easy enough to sort the array and then add up the first k elements.
# Or return nil if the length n of the array is less than k.
def better_algo_x(A, k):
    """better_algo_x returns the sum of the k smallest values in A. If A contains
    less than k values, then the result is None.
    """
    n = len(A)
    if n < k:
        return None
    B = sorted(A)
    sum = 0
    for i in range(k):
        sum += B[i]
    return sum

