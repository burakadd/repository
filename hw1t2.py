def _max2sort(_arg):
    return sorted(_arg, reverse=True)[:2]


_list = []
for i in range(int(input('N = '))):
    _list.append(int(input('{} number = '.format(i+1))))
print(_list)
print(*_max2sort(_list))
