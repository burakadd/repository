import typing
_c = "X"
_n = "O"
_list = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]


def print_grid(_arg):
    _e0 = '      1   2   3'
    _e = '   +___+___+___+'
    l1 = ' 1 | {} | {} | {} |'.format(_arg[0][0], _arg[0][1], _arg[0][2])
    l2 = ' 2 | {} | {} | {} |'.format(_arg[1][0], _arg[1][1], _arg[1][2])
    l3 = ' 3 | {} | {} | {} |'.format(_arg[2][0], _arg[2][1], _arg[2][2])
    print(_e0, '\n', _e, '\n', l1, '\n', _e, '\n', l2, '\n', _e, '\n', l3, '\n', _e)


def make_turn(_arg1):
    print("It's YOUR turn")
    abscisse = int(input("ROW number = ")) - 1
    ordinatus = int(input("COLUMN number = ")) - 1
    _arg1[abscisse][ordinatus] = 1


print_grid(_list)
make_turn(_list)
print_grid(_list)
