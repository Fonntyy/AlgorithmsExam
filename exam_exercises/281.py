# Q1
# USE
# This algorithm prints in ascending order all the elements of the maximum occurrence count.
# COMPLEXITY
# Best and worst case: theta(n^2)

# Q2
def better_algo_y(A):
    """Complexity is that of a sorting algorithm. The rest amounts for theta(n)."""
    B = sorted(A)
    if len(B) == 0:
        return 0
    count = 1
    maximum_count = 1
    for i in range(1, len(B)):
        if B[i] == B[i-1]:
            count += 1
            if count > maximum_count:
                maximum_count = count
        else:
            count = 1
    count = 1
    for i in range(len(B)):
        if i > 0 and B[i] == B[i-1]:
            count += 1
        else:
            count = 1
        if count == maximum_count:
            print(B[i])
