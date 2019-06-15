import typing
import sys
_list = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
pl1 = input("Name of first player is ")
pl2 = input("Name of second player is ")
while pl1 == pl2:
    print("It is name of first player")
    pl2 = input("Name of second player is ")
_dict = {pl1: "X", pl2: "O"} 


def _player(_arg):
    return pl1 if _arg % 2 else pl2


def print_grid(_arg):
    _e0 = '      1   2   3'
    _e = '   +___+___+___+'
    l1 = ' 1 | {} | {} | {} |'.format(_arg[0][0], _arg[0][1], _arg[0][2])
    l2 = ' 2 | {} | {} | {} |'.format(_arg[1][0], _arg[1][1], _arg[1][2])
    l3 = ' 3 | {} | {} | {} |'.format(_arg[2][0], _arg[2][1], _arg[2][2])
    _field =
    print(_e0, '\n', _e, '\n', l1, '\n', _e, '\n', l2, '\n', _e, '\n', l3, '\n', _e)


def make_turn(_arg1):
    print("It is {}'s turn".format(_player(turn_number)))
    while True:
        abscisse, ordinatus = -1, -1
        print("Enter row's number from set {1, 2, 3}")
        while abscisse < 0 or abscisse > 2:
            try:
                abscisse = int(input("ROW number = ")) - 1                     
            except ValueError:
                print("FAIL!!! ENTER CORRECTLY")
        print("Enter column's number from set {1, 2, 3}")
        while ordinatus < 0 or ordinatus > 2:
            try:
                ordinatus = int(input("COLUMN number = ")) - 1                     
            except ValueError:
                print("FAIL!!! ENTER CORRECTLY")
        if _arg1[abscisse][ordinatus] != "X" and _arg1[abscisse][ordinatus] != "O":
            _arg1[abscisse][ordinatus] = _dict.get(_player(turn_number))
            break
        else:
            print("WRONG TURN!!! THERE IS ANOTHER SYMBOL IN THIS CELL")


def check_win(_arg):
    for i in range(3):
        if _arg[0][i] == _arg[1][i] == _arg[2][i] and _arg[0][i] != " ":
            sys.exit("{} IS WINNER".format(_player(turn_number)))
        elif _arg[i][0] == _arg[i][1] == _arg[i][2] and _arg[i][2] != " ":
            sys.exit("{} IS WINNER".format(_player(turn_number)))
    if _arg[0][0] == _arg[1][1] == _arg[2][2] and _arg[0][0] != " ":
        sys.exit("{} IS WINNER".format(_player(turn_number)))
    elif _arg[0][2] == _arg[1][1] == _arg[2][0] and _arg[0][2] != " ":
        sys.exit("{} IS WINNER".format(_player(turn_number)))


def check_draw():
    if turn_number == 10:
        sys.exit("IT IS A DRAW")


print("LET'S PLAY")
turn_number = 1   
while True:
    make_turn(_list)
    print_grid(_list)
    check_win(_list)
    turn_number += 1
    check_draw()
