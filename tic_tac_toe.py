import typing
import sys


def _player(_arg1, _arg2, _arg3):
    return _arg1 if _arg3 % 2 else _arg2


def print_grid(_arg):
    [_e0, _e, l1, l2, l3] = ['      1   2   3', '   +___+___+___+',
                             ' 1 | {} | {} | {} |'.format(_arg[0][0], _arg[0][1], _arg[0][2]),
                             ' 2 | {} | {} | {} |'.format(_arg[1][0], _arg[1][1], _arg[1][2]),
                             ' 3 | {} | {} | {} |'.format(_arg[2][0], _arg[2][1], _arg[2][2])]
    print(_e0, '\n', _e, '\n', l1, '\n', _e, '\n', l2, '\n', _e, '\n', l3, '\n', _e)


def make_turn(_arg1, _arg2, _arg3, _arg4):
    _dict = {1: "X", 0: "O"}
    if _arg1[_arg2][_arg3] == "X" or _arg1[_arg2][_arg3] == "O":
        print("WRONG TURN!!! THERE IS ANOTHER SYMBOL IN THIS CELL")
        return False
    elif _arg2 < 0 or _arg2 > 2 or _arg3 < 0 or _arg3 > 2:
        print("WRONG TURN!!! YOU MUST ENTER VALUE FROM SET {1, 2, 3}")
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


def check_draw(_arg):
    if _arg == 10:
        return True
    return False


_list = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
pl1 = input("Name of first player is ")
pl2 = input("Name of second player is ")
while pl1 == pl2:
    print("It is name of first player")
    pl2 = input("Name of second player is ")
print("LET'S PLAY")
turn_number = 1
while True:
    print("It is {}'s turn".format(_player(pl1, pl2, turn_number)))
    abscisse, ordinatus = -1, -1
    while make_turn(_list, abscisse, ordinatus, turn_number) is False:
        while True:
            try:
                abscisse = int(input("ROW number = ")) - 1
                break
            except ValueError:
                print("FAIL!!! ENTER CORRECTLY")
        while True:
            try:
                ordinatus = int(input("COLUMN number = ")) - 1
                break
            except ValueError:
                print("FAIL!!! ENTER CORRECTLY")
    print_grid(_list)
    if check_win(_list) is True:
        sys.exit("{} IS WINNER".format(_player(pl1, pl2, turn_number)))
    if check_draw(turn_number):
        sys.exit("IT IS A DRAW")
    turn_number += 1
