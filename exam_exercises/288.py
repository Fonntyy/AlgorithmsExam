# Q1: returns the highest total sum of transaction amounts that have happened in a 10 day period
import copy


# Q2: Complexity
# Best and worst case: theta(n^2)

# Q3
class Transaction:
    def __init__(self, date, amount):
        self.date = date
        self.amount = amount

    def __repr__(self):
        return f'{self.date} : {self.amount}'


T = [
    Transaction(20, 40),
    Transaction(6, 20),
    Transaction(2, 30),
    Transaction(14, 25)
]


def copy_and_sort_by_date(T):
    return sorted(copy.deepcopy(T), key=lambda x: x.date)


def better_algo_y(T):
    """Complexity that of a sorting algorithm."""
    S = copy_and_sort_by_date(T)
    i = 0
    j = 0
    curr_sum = 0
    curr_max = 0

    while j < len(S):
        if S[j].date - S[i].date <= 10:
            curr_sum += S[j].amount
            j += 1
            if curr_sum > curr_max:
                curr_max = curr_sum
        else:
            curr_sum -= S[i].amount
            i += 1

    return curr_max
