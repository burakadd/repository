from socket import create_connection, SHUT_WR, socket as so, getaddrinfo as ge

# with create_connection(('google.by', 80)) as s:
#     s.send(b'GET / HTTP/1.1\r\n\r\n')
#     s.shutdown(SHUT_WR)
#     data = s.recv(100000)
#     print(data.decode())

family, type, proto, name, addr = ge("127.0.0.1", 1234)[0]
server = so(family, type, proto)
server.bind(addr)
server.listen(5)
client1 = create_connection(('127.0.0.1', 1234))
client2, addr = server.accept()

client2.send(b'Hello!')
client2.shutdown(SHUT_WR)

data = client1.recv(1000)
print(data)

client2.close()
client1.close()
