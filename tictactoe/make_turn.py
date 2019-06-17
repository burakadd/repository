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
