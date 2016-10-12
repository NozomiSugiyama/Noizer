#! /usr/local/bin/python3
# -*- coding: utf-8 -*-

import socket
from datetime import datetime
import json

STOP_ALARM = 0


address = ('192.168.43.151', 6789)
max_size = 1000

print('Starting the client at', datetime.now())
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(address)
client.sendall(json.dumps({ 'flag': STOP_ALARM }).encode('utf-8'))
data = client.recv(max_size)
print('At', datetime.now(), 'someone replied', data)
client.close()