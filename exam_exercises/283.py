# Q1 and Q2 - It is both NP and P because it can be solved.

def uniform_pairing_exists(A):
    B = sorted(A)
    v = B[0] + B[len(B) - 1]
    i = 1
    j = len(B) - 2
    while i < j:
        if B[i] + B[j] != v:
            return False
        i += 1
        j -= 1
    return True
