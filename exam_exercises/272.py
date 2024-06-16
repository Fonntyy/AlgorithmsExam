# Q1
def verify(k, A, I):
    return solve(k, A) >= k


# Q2
def solve(k, A):
    B = []  # B is a list of all possible pair sums
    for i in range(len(A)):
        for j in range(i, len(A)):
            B.append(A[i] + A[j])
    B = sorted(B)
    i = 0
    j = 0
    while j < len(B):
        if B[i] == B[j]:
            j += 1
            if j - i >= k:
                return True
        else:
            j += 1
            i = j
    return False
