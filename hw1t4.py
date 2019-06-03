from math import factorial


def cos_tailor_member(i, _arg):
    return (-1 ** i) * (_arg ** (2 * i)) / factorial(2 * i)


def cos_into_tailor(n, _arg):
    return 1 + sum(map(lambda n: cos_tailor_member(n, _arg), range(n)))


N = int(input("n = "))
_argument = float(input("x = "))

print(cos_into_tailor(N, _argument))
