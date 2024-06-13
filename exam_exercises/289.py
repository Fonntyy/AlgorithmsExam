def min_deap_add(H, x):
    H.append(x)
    i = len(H) - 1
    while (i - 1) // 2 >= 0 and H[(i - 1) // 2] > H[i]:
        H[i], H[(i - 1) // 2] = H[(i - 1) // 2], H[i]
        i = (i - 1) // 2


def create_min_heap(lst):
    H = []
    for el in lst:
        min_deap_add(H, el)
    return H
