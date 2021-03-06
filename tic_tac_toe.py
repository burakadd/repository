
import sys
from tictactoe import tictactoe_func as F


def _player(_arg1, _arg2, _arg3):
    return _arg1 if _arg3 % 2 else _arg2


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
    while not F.make_turn(_list, abscisse, ordinatus, turn_number):
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
    F.print_grid(_list)
    if F.check_win(_list) is True:
        sys.exit("{} IS WINNER".format(_player(pl1, pl2, turn_number)))
    if F.check_draw(turn_number):
        sys.exit("IT IS A DRAW")
    turn_number += 1
