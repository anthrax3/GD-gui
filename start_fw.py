#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import subprocess
import sys
from time import sleep
from ConfigParser import ConfigParser
import subprocess
import re
import os
import config_parser as CP
import signal
import shutil
from distutils.dir_util import copy_tree


def start_fwbuilder():

    fw_path = CP.get_configs()['fw_path']
    file_name = CP.get_configs()['fwb_file_name']
    run_fwb = fw_path + file_name

    subprocess.Popen(["fwbuilder", "-f",run_fwb])
def check_if_runs():
    try:
        s = subprocess.Popen(["ps", "aux"], stdout=subprocess.PIPE)
        for x in s.stdout:
            res = re.search("fwbuilder",x)
            res2 = re.search("fwbuilder-ahtapot",x)
            if res is not None and res2 is None:
                return True
        return False
    except IOError:
        check_if_runs()

def kill_fw():
    s = subprocess.Popen(["ps", "aux"], stdout=subprocess.PIPE)
    out, err = s.communicate()

    for line in out.splitlines():
            if "fwbuilder" in line and not "fwbuilder-ahtapot" in line:
                    pid = int(line.split(None,1)[1].split()[0])
                    os.kill(pid,signal.SIGKILL)

def kill_gui_user(username):
    s = subprocess.Popen(["ps", "aux"], stdout=subprocess.PIPE)
    out, err = s.communicate()

    for line in out.splitlines():
            if "gdys-gui" in line and not username in line:
                    pid = int(line.split(None,1)[1].split()[0])
                    os.kill(pid,signal.SIGKILL)


def kill_gui():
    sleep(1)
    s = subprocess.Popen(["ps", "aux"], stdout=subprocess.PIPE)
    out, err = s.communicate()

    for line in out.splitlines():
            if "gdys-gui" in line:
                    pid = int(line.split(None,1)[1].split()[0])
                    os.killpg(pid,signal.SIGKILL)
