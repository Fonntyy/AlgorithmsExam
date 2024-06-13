def square_root(n):
    low = 0
    high = n
    while low <= high:
        mid = (low + high) // 2
        if mid ** 2 < n:
            low = mid + 1
        else:
            high = mid - 1
    return high
