def count(_arg1, _arg2=1):
    while True:
        yield _arg1
        _arg1 += _arg2
    
    
for i in count(7, 2):
    print(i)
    if i>15:
        break
