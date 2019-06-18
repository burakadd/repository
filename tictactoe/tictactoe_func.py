def check_draw(_arg):
    if _arg == 9:
        return True
    return False


def print_grid(_arg):
    [_e0, _e, l1, l2, l3] = ['      1   2   3', '   +___+___+___+',
                             ' 1 | {} | {} | {} |'.format(_arg[0][0], _arg[0][1], _arg[0][2]),
                             ' 2 | {} | {} | {} |'.format(_arg[1][0], _arg[1][1], _arg[1][2]),
                             ' 3 | {} | {} | {} |'.format(_arg[2][0], _arg[2][1], _arg[2][2])]
    print(_e0, _e, l1, _e, l2, _e, l3,  _e, sep = '\n')


def make_turn(_arg1, _arg2, _arg3, _arg4):
    _dict = {1: "X", 0: "O"}
    if _arg2 < 0 or _arg2 > 2 or _arg3 < 0 or _arg3 > 2:
        print("YOU MUST ENTER VALUE FROM SET {1, 2, 3}")
        return False
    if _arg1[_arg2][_arg3] == "X" or _arg1[_arg2][_arg3] == "O":
        print("WRONG TURN!!! THERE IS ANOTHER SYMBOL IN THIS CELL")
        return False
    _arg1[_arg2][_arg3] = _dict.get(_arg4 % 2)
    return True


def check_win(_arg):
    for i in range(3):
        if _arg[0][i] == _arg[1][i] == _arg[2][i] and _arg[0][i] != " ":
            return True
        elif _arg[i][0] == _arg[i][1] == _arg[i][2] and _arg[i][2] != " ":
            return True
    if _arg[0][0] == _arg[1][1] == _arg[2][2] and _arg[0][0] != " ":
        return True
    elif _arg[0][2] == _arg[1][1] == _arg[2][0] and _arg[0][2] != " ":
        return True
    return False
