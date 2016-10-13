#! /usr/local/bin/python3
# -*- coding: utf-8 -*-

import socket
from datetime import datetime
import json

STOP_ALARM = 0


max_size = 1024
ip_list = []
for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]:
    try:
        s.connect(('8.8.8.8', 80))
    except:
        print('Network is unreachable')
        os._exit(1)

    ip = s.getsockname()
    for n in ip:
        name = ip[0]
        ip_list.append(name)
    s.close()

address = (ip_list[0], 6789)

print('Starting the client at', datetime.now())
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(address)
client.sendall(json.dumps({'flag': STOP_ALARM}).encode('utf-8'))
data = client.recv(max_size)
print('At', datetime.now(), 'someone replied', data)
client.close()
