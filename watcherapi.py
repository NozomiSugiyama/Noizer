import os, sys, time
import signal
from datetime import datetime
import socket


class WatcherApi:
    def __init__(self, address, port, pid):
        self.address = (address, port)
        self.max_size = 1000
        self.pid = pid

    def start(self):

        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            server.bind(self.address)
        except Exception:
            print('Waiting for the end of the process.')
            time.sleep(10)

        print('Starting the server at', datetime.now())
        print('Waiting for a client to call.')
        while True:
            server.listen(5)

            client, addr = server.accept()
            data = client.recv(self.max_size)

            print('At', datetime.now(), client, 'said', data)
            client.sendall(b'kill process')
            self._process_kill()
            client.close()
        server.close()

        print('Reset connection')

    def _process_kill(self):
        print('kill process id : ' + str(self.pid))
        try:
            os.kill(self.pid, signal.SIGKILL)
            print('killed :' + str(self.pid))
        except PermissionError as inst:
            print(inst.args)
        except ProcessLookupError as inst:
            print(inst.args)

if __name__ == '__main__':

    print('--- watcherapi.py : ' + str(os.getpid()) + ' ---')

    argv_list = sys.argv
    argc = len(argv_list)

    if argc != 2:
        print('Not enough arguments')
        quit()

    watcher_api = WatcherApi(socket.gethostbyname(socket.gethostname()), 6789, int(argv_list[1]))
    watcher_api.start()


