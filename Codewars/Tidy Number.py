def tidyNumber(n):
    return n == int("".join(sorted(list(str(n)))))

print(tidyNumber(12345))
print(tidyNumber(12365))