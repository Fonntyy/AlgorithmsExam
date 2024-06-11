def algo_y(A):
    """Returns True if A contains more than three distinct elements."""
    B = sorted(A)  # Merge sort - complexity theta(n * log n)
    n = len(A)
    x = 1
    for i in range(1, n):  # complexity theta(n)
        if B[i] != B[i - 1]:
            x = x + 1
    if x > 3:
        print(x)  # for debugging
        return True
    else:
        print(x)  # for debugging
        return False

# COMPLEXITY: theta(n * log n)


# STRATEGY: "We can simply scan the input array and build an array of at
# most three elements to store the first three distinct values"
def better_algo_y(A):
    """Returns True if A contains more than three distinct elements with
    strictly better time complexity than algo_y.
    """
    distinct_elements = []
    for i in range(len(A)):
        # IS THE CURRENTLY LOOKED AT ELEMENT DISTINCT TO DISTINCT ELEMENTS?
        is_distinct = True
        # Constant complexity as distinct elements is only allowed to have
        # at most three elements.
        for distinct_el in distinct_elements:
            if A[i] == distinct_el:
                is_distinct = False
        if is_distinct:
            distinct_elements.append(A[i])
        if len(distinct_elements) > 3:
            print(len(distinct_elements))  # for debugging
            return True
    print(len(distinct_elements))  # for debugging
    return False


# COMPLEXITY: theta(n)
