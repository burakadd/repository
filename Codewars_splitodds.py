# 0 -> Split into two odd numbers, that are closest to each other.
#      (e.g.: 8 -> 3,5)
# 1 -> Split into two odd numbers, that are most far from each other.
#      (e.g.: 8 -> 1,7)
# 2 -> All new odd numbers from the splitting should be equal and the maximum possible number.
#      (e.g.: 8 -> 1, 1, 1, 1, 1, 1, 1, 1)
# 3 -> Split into 1s.
#      (e.g.: 8 -> 1, 1, 1, 1, 1, 1, 1, 1)
# The new numbers (from the splitting) have always to be in ascending order.
# So in the array every even number is replaced by the new odd numbers from the splitting.
import math

def max_odd(num):
    n = math.ceil(math.sqrt(num))
    while num % n or not n % 2:
        n -= 1
    return [n for i in range(num // n)]


def split_all_even_numbers(numbers, way):
    mappers = {0: lambda i: [i // 2 - 1, i // 2 + 1],
               1: lambda i: [1, i - 1],
               2: lambda i: max_odd(i),
               3: lambda i: [1 for j in range(i)]}

    return list(map(mappers[way] , numbers))

_list = [1, 2, 4, 6, 8, 12, 11]
print(split_all_even_numbers(_list, 2))






