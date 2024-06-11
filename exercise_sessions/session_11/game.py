def minimal_cost_game(A,B):
    return DP(A, 0, B, 0)


def value(C):
    return C[0]


def suit(C):
    return C[1]


def DP(A, i, B, j):
    if i >= len(A) and j >= len(B):
        return 0
    elif j >= len(B):
        cost = 0
        while i < len(A):
            cost += value(A[i])
            i += 1
        return cost
    elif i >= len(A):
        cost = 0
        while j < len(B):
            cost += value(B[j])
            j += 1
        return cost
    else:
        cost = min(
            DP(A, i+1, B, j) + value(A[i]),
            DP(A, i, B, j+1) + value(B[j])
        )
        if value(A[i]) == value(B[j]) or suit(A[i]) == suit(B[j]):
            cost = min(
                cost,
                DP(A, i+1, B, j+1)
            )
        return cost
