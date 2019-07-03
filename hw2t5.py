def chain(*_iters):   
    return (i for it in _iters for i in it)  # это не генератор, ты написал функцию, которая возвращает кортеж

# вот это генератор:
def chain2(*iters):
    for iterable in iters:
        for item in iterable:
            yield item


assert [i for i in chain(range(3), range(1, 4), range(2, 5))] == \
[0, 1, 2, 1, 2, 3, 2, 3, 4]
