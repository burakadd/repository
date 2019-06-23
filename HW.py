from random import shuffle
a = list(range(25))
shuffle(a)


def _prime(_arg):
    if _arg % 2 == 0:
        return False
    d = 3
    while d**2 <= _arg and _arg % d != 0:
        d += 2
    if d**2 > _arg:
        return True
    else:
        return False

print(list(filter(lambda i: _prime(i), a)))
