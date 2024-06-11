def square_root(n):
    low = 0
    high = n

    while low <= high:
        mid = (low + high) // 2
        if mid * mid > n:
            high = mid - 1
        else:
            low = mid + 1

    return high

print(square_root(15))
print(square_root(16))
print(square_root(17))