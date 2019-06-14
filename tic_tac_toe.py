import typing
#_c = 
#_n = "O"
_list = [[" ", " ", " "], 
[ " ", " ", " "], 
[" ", " ", " "]]

pl1 = input("Name of first player is ")
pl2 = input("Name of second player is ")
while pl1 == pl2:
    print("It is name of first player")
    pl2 = input("Name of second player is ")


_dict = {pl1: "X", pl2: "O"} 


def _player(_arg):
    if _arg % 2:
        return pl1
    else:
        return pl2 
        

def print_grid(_arg):
    _e0 = '      1   2   3'
    _e = '   +___+___+___+'
    l1 = ' 1 | {} | {} | {} |'.format(_arg[0][0], _arg[0][1], _arg[0][2])
    l2 = ' 2 | {} | {} | {} |'.format(_arg[1][0], _arg[1][1], _arg[1][2])
    l3 = ' 3 | {} | {} | {} |'.format(_arg[2][0], _arg[2][1], _arg[2][2])
    print(_e0, '\n', _e, '\n', l1, '\n', _e, '\n', l2, '\n', _e, '\n', l3, '\n', _e)

print_grid(_list)

def make_turn(_arg1):
    while True:
        abscisse, ordinatus = -1, -1
        print("It is {}'s turn".format(_player(turn_number)))
        print("Select row's number from set {1, 2, 3}")
        while abscisse < 0 or abscisse > 2:
            try:
                abscisse = int(input("ROW number = ")) - 1                     
            except ValueError:
                print("FAIL!!! ENTER CORRECTLY")
        print("Select column's number from set {1, 2, 3}")
        while ordinatus < 0 or ordinatus > 2:
            try:
                ordinatus = int(input("COLUMN number = ")) - 1                     
            except ValueError:
                print("FAIL!!! ENTER CORRECTLY")
        if _arg1[abscisse][ordinatus] != "X" and _arg1[abscisse][ordinatus] != "O":
           _arg1[abscisse][ordinatus] = _dict.get(_player(turn_number))
           break
        else:
            print("WRONG TURN!!! THERE IS ANOTHER SYMBOL IN YHIS CELL")

def check_win(_arg):
    for i in _arg:
        if len(set(i)) == 1:
            print("{} IS WINNER".format(_player(turn_number))
print("LET'S PLAY")
turn_number = 1   
for i in range(3):
    make_turn(_list)
    turn_number += 1
    print_grid(_list)




