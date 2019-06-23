import functools


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


def _switchcase(_arg):
    _dict = {"sum": functools.reduce(lambda i, j: i + j, _arg),
             "multiply": functools.reduce(lambda i, j: i * j, _arg),
             "join": map(int, "".join(map(str, _arg))),
             "union": set(_arg),

             "negated": map(lambda i: -i, _arg),
             "inverted": map(lambda i: i**(-1), _arg),
             "squared": map(lambda i: i**2, _arg),

             "odds": filter(lambda i: i % 2 == 1, _arg),
             "evens": filter(lambda i: i % 2 == 0, _arg),
             "simples": filter(lambda i: _prime(i), _arg)}
    return None


a = [5, 6, 7]
print(map(int, "".join(list(map(str, a)))))