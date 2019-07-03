import random
import functools

def _join(_arg):
    _list = [i*10**(len(_arg) - j) for j, i in enumerate(_arg, 1)]
    return functools.reduce(lambda i,j: i + j, _list)


def _prime(_arg):
    if not _arg % 2:
        return False
    d = 3
    while d**2 <= _arg and _arg % d:
        d += 2
    if d**2 > _arg:
        return True
    else:
        return False


def _switchcase(_arg, *funcs):
    _switchcaselist = {"sum": functools.reduce(lambda i, j: i + j, _arg),
             "multiply": functools.reduce(lambda i, j: i * j, _arg),
             "join": _join(_arg),
             "union": set(_arg),
             "reversed": reversed(_arg),

             "negated": list(map(lambda i: -i, _arg)),
             "inverted": list(map(lambda i: i**(-1), _arg)),
             "squared": list(map(lambda i: i**2, _arg)),

             "odds": list(filter(lambda i: i % 2, _arg)),
             "evens": list(filter(lambda i: not i % 2, _arg)),
             "simples": list(filter(lambda i: _prime(i), _arg))}
    return _switchcaselist[func]


n = int(input("n = "))    
_data = [random.randint(1, 9) for i in range(n)]
print(_data)
for func in reversed(input("input funcs ").split(" ")):
    print(func)
    _data = _switchcase(_data, func)
    print(_data)


             "join": _join(_arg),
             "union": set(_arg),
             "reversed": reversed(_arg),
reducer = {"sum": lambda i, j: i + j, "multiply": lambda i, j: i * j,
}
mappers = {"negated": lambda i: -i, "inverted": lambda i: i ** (-1),"squared": lambda i: i ** 2}
filters = {"odds": lambda i: i % 2, "evens": lambda i: not i % 2, "simples": lambda i: _prime(i)}