from random import randint


def check_input():
    while True:
        try:
            k = int(input("a="))
            break
        except ValueError:
            print('FAIL! ENTER CORRECTLY')
    return k


b = randint(0, 10)
print('try guessing')
while check_input() != b:
    print('have not guessed')
print('SUCCESS')
