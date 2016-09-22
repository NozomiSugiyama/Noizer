import os, sys
import signal
from datetime import datetime
import socket

class NoizerApi():
    def __init__(self, address, port, pid):
        self.address = (address, port)
        self.max_size = 1000
        self.pid = pid

    def start(self):
        print('Starting the server at', datetime.now())
        print('Waiting for a client to call.')

        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind(self.address)
        server.listen(5)

        client, addr = server.accept()
        data = client.recv(self.max_size)

        print('At', datetime.now(), client, 'said', data)
        client.sendall(b'kill process')
        self._process_kill()
        client.close()
        server.close()

    def _process_kill(self):
        os.kill(self.pid, signal.SIGKILL)

if __name__ == '__main__':

    argv_list = sys.argv
    argc = len(argv_list)

    if argc != 2:
        print('Not enough arguments')
        quit()

    noizer_api = NoizerApi(socket.gethostbyname(socket.gethostname()), 6789, int(argv_list[1]))
    noizer_api.start()

    print("debug")

