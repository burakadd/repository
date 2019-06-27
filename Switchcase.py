import random
import functools


def _prime(_arg):
    if _arg % 2:
        d = 3
        while d**2 <= _arg and _arg % d:
            d += 2
        if d**2 > _arg:
            return True
    else:
        return False
   

reducers = {"sum": lambda i, j: i + j, 
    "multiply": lambda i, j: i * j,
    "join": lambda i, j: 10 * i + j, 
    "union": lambda i, j: [*i, j] if not j in i else i,
    "reversed": lambda i, j: [j, *i]}
mappers = {"negated": lambda i: -i, 
    "inverted": lambda i: i ** -1, 
    "squared": lambda i: i ** 2}
filters = {"odds": lambda i: i % 2, 
    "evens": lambda i: not i % 2, 
    "simples": lambda i: _prime(i)}
reducerinitial = {"sum": 0, 
    "multiply": 1,
    "join": 0,
    "union": [],
    "reversed": []}

_data = [random.randint(1, 9) for i in range(int(input("n = ")))]
print(_data)
_reducer, _mapper, _filter = input("input funcs").split(" ")
print(functools.reduce(reducers[_reducer], map(mappers[_mapper], filter(filters[_filter], _data)), reducerinitial[_reducer]))
