a = [1,2,3,4]
b = list(range(5))
print(list(filter(lambda i: i not in a, b)))