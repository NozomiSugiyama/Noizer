#! /bin/python
# -*- coding: utf-8 -*-

import subprocess
import datetime
import time, os

def main():
    print('--- Start Noizer ---')
    pid = subprocess.Popen('python noizer.py', shell=True).pid
    print(str(pid))
    subprocess.call("python processkiller.py " + str(pid) + " &", shell=True)

if __name__ == '__main__':
    print('--- main.py : ' + str(os.getpid()) + ' ---')

    while True:
        alarm_hour = 4
        alarm_minute = 1

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
