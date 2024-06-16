import queue
import math


# Q1
def check_connectivity(X, Y, r):
    """Given the coordinates of all the sensors stored in arrays X and Y,
    such that sensor i is located at coordinates (X [i], Y [i]), and given
    the communication range r, returns true if all sensors can transmit
    their data to the base station, or false if one or more sensors can
    not do that."""
    n = len(X)
    D = [False] * n
    Q = queue.Queue()
    Q.put((0, 0))
    while not Q.empty():
        x, y = Q.get()
        for i in range(n):
            if not D[i] and (X[i] - x)**2 + (Y[i] - y)**2 <= r**2:
                D[i] = True
                Q.put((X[i], Y[i]))
    for i in range(n):
        if not D[i]:
            return False
    return True

# Complexity: theta(n^2)


# Q2
def minimal_connectivity_range(X, Y, t):
    """ Given the coordinates of all the sensors stored in arrays X and Y,
    and given a precision threshold t, returns the minimal radio range r that
    would guarantee full connectivity."""
    r_min = 0
    r_max = 0
    for i in range(len(X)):
        if X[i]**2 + Y[i]**2 > r_max**2:
            r_max = math.sqrt(X[i]**2 + Y[i]**2)
    while r_max - r_min > t:
        r = (r_max + r_min) / 2
        if check_connectivity(X, Y, r):
            r_max = r
        else:
            r_min = r
    return (r_max + r_min) / 2

# Complexity: theta(n^2*log2(r_max/t))
