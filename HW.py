a = [1, 1, 1, 2, 3, 4, 5, 6]

print(list(filter(lambda i: a.remove(i) if i in a, a)))
