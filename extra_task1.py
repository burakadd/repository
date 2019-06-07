#составить из списка чисел максимальное число
from random import randint

_list = ['6', '67', '678', '6781']
#_list = [ str(randint(1,10000)) for i in range(int(input('N = ')))]
print(_list)
def _func(_arg):
    _List = []
    while len(_arg): #append
        a = min([len(i) for i in _arg])
        _List.append(max([i[0] for i in map(lambda i: (i[:a], i), _arg)]))
        _arg.remove(_List[-1])      
    _len = len(_List)    
    while _len: #sort
        _len -= 1
        for i in _List:
            for j in _List[_List.index(i)+1:]:
                if j.find(i) == 0 and int(j[len(i)]) > int(i[0]):
                    a = _List.index(i)
                    b = _List.index(j)
                    _List[a], _List[b] = _List[b], _List[a]    
    return ''.join(_List)
    
print(_func(_list))
