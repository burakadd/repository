def disarium_number(number):
    list_number =list(str(number))
    return "Disarium !!" if sum(map(lambda i: int(i) ** (list_number.index(i)+1), list_number)) == number else "Not !!"


print(disarium_number(89))
print(disarium_number(88))
print(disarium_number(1000))