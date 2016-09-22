#! /bin/python
# -*- coding: utf-8 -*-

from noizer import noizer
import datetime
import subprocess
import time

def main():
    print('--- Start Noizer ---')
    pid = subprocess.Popen('python noizer.py', shell=True).pid
    print(str(pid))
    subprocess.call("python processkiller.py " + str(pid) + " &", shell=True)

if __name__ == '__main__':

    alarm_hour = 3
    alarm_minute = 41

    alarm_repeat_minute = 30
    alarm_repeat_num = 4

    now = datetime.datetime.today()

    if now.hour == alarm_hour and now.minute == alarm_minute:
        for i in range(alarm_repeat_num):
            noizer()
            time.sleep(alarm_repeat_minute * 60)

    # list内方式
    # Reactiveプログラミング
    #
    # map
    time.sleep(30)
