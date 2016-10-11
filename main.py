#! /bin/python
# -*- coding: utf-8 -*-
import subprocess
import datetime
import time, os


def main():
    print('--- Start Noizer ---')
    noizer_pid = subprocess.Popen('python watcher.py', shell=True).pid
    print(str(noizer_pid))

    # tcp_server process
    # process_killer_pid = subprocess.Popen("python watcherapi.py " + str(noizer_pid), shell=True).pid
    # try:
    #     os.kill(process_killer_pid, signal.SIGKILL)
    # except PermissionError as inst:
    #     print(inst.args)
    # except ProcessLookupError as inst:
    #     print(inst.args)


if __name__ == '__main__':
    print('--- main.py : ' + str(os.getpid()) + ' ---')

    while True:
        alarm_hour = 5
        alarm_minute = 24

        alarm_repeat_minute = 30
        alarm_repeat_num = 4

        now = datetime.datetime.today()

        if now.hour == alarm_hour and now.minute == alarm_minute:
            for i in range(alarm_repeat_num):
                main()
                time.sleep(alarm_repeat_minute * 60)

        # list内方式
        # Reactiveプログラミング
        #
        # map
        time.sleep(30)
