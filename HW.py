import math


def max_odd(num):
    n = math.ceil(math.sqrt(num))
    while num % n or not n % 2:
        n -= 1
    return [n for i in range(num // n)]


print(max_odd(8))


# numbers = [1, 2, 3, 4, 12, 18]
# print(list(map(lambda i: max_odd(i) for j in range(i // max_odd(i)) if i % 2, numbers)))
