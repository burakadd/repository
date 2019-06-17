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
