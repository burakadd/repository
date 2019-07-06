def extra_perfect(n):
    return [i for i in range(1, n+1) if int(bin(i)[-1])]

print(extra_perfect(39))
print(bin(40)[-1])