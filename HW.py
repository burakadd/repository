 from socket import create_connection, SHUT_WR, socket, getaddrinfo
# #
# # with create_connection(('google.by', 80)) as s:
# #     s.send(b'GET / HTTP/1.1\r\n\r\n')
# #     s.shutdown(SHUT_WR)
# #     data = s.recv(100000)
# #     print(data.decode())
#
# family, type, proto, name, addr = getaddrinfo("127.0.0.1", 12345)[0]
# server = socket(family, type, proto)
# server.bind(addr)
# server.listen(5)
#
#
#
#
# client1 = create_connection(('127.0.0.1', 12345))
# client2, addr = server.accept()
#
# client2.send(b'GET HTTP/1.0 404 OK')
# client2.shutdown(SHUT_WR)
#
# data = client1.recv(1000)
# print(data)
#
# client2.close()
# client1.close()
import socket


sock = socket.socket
sock.bind(("", 12345))
sock.listen(8)

conn, addr = sock.accept()

print('connected:', addr)

while True:
    data = conn.recv(1024)
    if not data:
        break
    conn.send(data.upper())

conn.close()

