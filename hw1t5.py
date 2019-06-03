_dict = {'+': lambda x, y: x + y,
         '-': lambda x, y: x - y,
         '*': lambda x, y: x * y,
         '/': lambda x, y: x / y
         }
a = input('math problem =').split(" ")

while True:
    for i, j in enumerate(a):
        if j == "/" or j == "*":
            a[i - 1] = _dict[j](float(a[i - 1]), float(a[i + 1]))
            a.pop(i)
            a.pop(i)
            break
    else:
        break

while True:
    for i, j in enumerate(a):
        if j == "+" or j == "-":
            a[i - 1] = _dict[j](float(a[i - 1]), float(a[i + 1]))
            a.pop(i)
            a.pop(i)
            break
    else:
        break

print(*a)
