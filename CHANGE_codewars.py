from functools import reduce

def change_count(change):
    CHANGE = {"penny": 0.01,
    "nickel": 0.05,
    "dime": 0.10,
    "quarter": 0.25,
    "dollar": 1.00}

    return reduce(lambda acc, i: acc + i, [CHANGE[i] for i in change])


