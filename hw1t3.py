def _func(_arg):
    return(sorted(_arg, key = bool))

_list = []
for i in range(int(input('N = '))):
    _list.append(int(input('{} number = '.format(i+1))))
print(_list)
print(_func(_list))
