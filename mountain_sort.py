def mount_sort(A):
    # if the array has only zero or one element than it returns the array itself
    if len(A) < 2:
        return A
    # it uses the insertion sort to sort the elements first in the increasing order
    for i in range(1, len(A)):
        j = i
        while j > 0 and A[j] < A[j - 1]:
            A[j], A[j - 1] = A[j - 1], A[j]
            j = j - 1
    # it reverses the second half of the array
    i = len(A) // 2
    j = len(A) - 1
    while i < j:
        A[i], A[j] = A[j], A[i]
        i = i + 1
        j = j - 1
    return A


print(mount_sort([1, 2, 1, -3]))
print(mount_sort([1, 2, 1, 0, -3]))
print(mount_sort([4, 7, 4]))
print(mount_sort([9, 6, 5]))
print(mount_sort([1, 2, 7, 8, 9]))
print(mount_sort([4, 2]))
print(mount_sort([2, 6]))
print(mount_sort([2]))
