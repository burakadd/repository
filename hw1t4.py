from math import factorial

def cos_tailor_member(i, _arg):
    return (-1**i)*(_arg**(2*i))/factorial(2*i)
    
def cos_into_tailor(n, _arg):
    return 1 - sum(map(lambda x: cos_tailor_member(i, _arg), range(n)))
    
N = int(input("n = ")
_argument = int(input("x = ")

print(cos_into_tailor(N, _argument))
