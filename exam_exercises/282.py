def compare_intervals(a1, b1, a2, b2):
    if a1 > b1:
        a1, b1 = b1, a1
    if a2 > b2:
        a2, b2 = b2, a2
    # KNOW: [a1, b1] and [a2, b2] are valid intervals
    if b1 < a2 or b2 < a1:
        return "disjoint"
    elif b1 == a2 or b2 == a1:
        return "touch"
    elif a1 == a2 or b1 == b2:
        return "1 equals 2"
    elif a1 <= a2 and b2 <= b1:
        return "1 covers 2"
    elif a2 <= a1 and b1 <= b2:
        return "2 covers 1"
    else:
        return "partial"
