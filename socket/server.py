from socket import getaddrinfo, socket, SHUT_WR
from shared import recv_data, send_data
# from socket import SOCK_STREAM
# from socket import AF_INET
# from socket import IPPROTO_IPV4


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

family, socktype, proto, name, addr = getaddrinfo('127.0.0.1', 1234)[0]
s = socket(family, socktype, proto)
s.bind(addr)
s.listen(1)
client, addr = s.accept()

while True:
    grid = recv_data(client)
    if not grid:
        break
    print(grid)
    if check_win(grid['grid']):
        send_data(client, 'smth won')
    else:
        send_data(client, 'draw')

client.shutdown(SHUT_WR)
client.close()


