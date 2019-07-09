from typing import Dict
import json
import socket


def dump_data(obj):
    return json.dumps(obj).encode()


def load_data(data):
    return json.loads(data.decode())


def send_data(s, obj):
    data = dump_data(obj)
    n = len(data)
    s.send(n.to_bytes(4, 'little'))
    s.send(data)


def recv_data(s):
    data = s.recv(4)
    if not data:
        return None
    n = int.from_bytes(data, 'little')
    data = s.recv(n)
    return load_data(data)
