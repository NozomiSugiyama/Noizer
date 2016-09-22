#! /bin/python
# -*- coding: utf-8 -*-

from noizer import noizer
import datetime
import subprocess
import time

if __name__ == '__main__':
    print('--- Start Noizer ---')
    pid = subprocess.Popen('python noizer.py', shell=True).pid
    print(str(pid))
    subprocess.call("python processkiller.py " + str(pid) + " &", shell=True)
