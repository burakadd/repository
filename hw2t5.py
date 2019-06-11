def chain(*_iters):   
    return (i for it in _iters for i in it)          
                        
assert [i for i in chain(range(3), range(1, 4), range(2, 5))] == \
[0, 1, 2, 1, 2, 3, 2, 3, 4]
