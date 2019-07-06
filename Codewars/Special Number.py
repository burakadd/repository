def special_number(number):
    if all(sign in range(6) for sign in map(int, list(str(number)))):
        return "Special!!"
    return "NOT!!"

print(special_number(555))
print(special_number(567))
print(special_number(777))