def print_grid(_arg):
    [_e0, _e, l1, l2, l3] = ['      1   2   3', '   +___+___+___+',
                             ' 1 | {} | {} | {} |'.format(_arg[0][0], _arg[0][1], _arg[0][2]),
                             ' 2 | {} | {} | {} |'.format(_arg[1][0], _arg[1][1], _arg[1][2]),
                             ' 3 | {} | {} | {} |'.format(_arg[2][0], _arg[2][1], _arg[2][2])]
    print(_e0, '\n', _e, '\n', l1, '\n', _e, '\n', l2, '\n', _e, '\n', l3, '\n', _e)