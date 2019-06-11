def chain(*iters):   
    return (i for it in iters for i in it)          
                        
assert [i for i in chain(range(3), range(1, 4), range(2, 5))] == \
[0, 1, 2, 1, 2, 3, 2, 3, 4]
