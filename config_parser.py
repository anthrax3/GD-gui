#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ConfigParser import ConfigParser
import os
import base64


Config = ConfigParser()

abs_path = os.path.abspath(__file__)
path_list = abs_path.split("/")
del path_list[-1]
path_name = "/".join(path_list)
full_path = path_name + "/"

Config.read(full_path + "config.ini")
#reading from config sections
def ConfigSectionMap(section):
    dict1 = {}
    options = Config.options(section)
    for option in options:
        try:
            dict1[option] = Config.get(section, option)
            if dict1[option] == -1:
                DebugPrint("Gec  %s" % option)
        except:
            print("Hata : %s!" % option)
            dict1[option] = None
    return dict1


def get_configs():
    Config.read(full_path + "config.ini")
    config = {}
    #Path Configs
    config["fw_path"] = ConfigSectionMap("Paths")['fw_path']
    config["std_out_err"] = ConfigSectionMap("Paths")['std_out_err']
    config["fwb_file_name"] = ConfigSectionMap("Paths")['fwb_file_name']

    config["git_master_branch"] = ConfigSectionMap("Git")['master_branch']
    config["git_project_name"] = ConfigSectionMap("Git")['project_name']
    config["git_project_id"] = ConfigSectionMap("Git")['project_id']

    return config

def get_path_configs():
    Config.read(full_path + "config.ini")
    config = {}
    #Path Configs
    config["fw_path"] = ConfigSectionMap("Paths")['fw_path']
    config["std_out_err"] = ConfigSectionMap("Paths")['std_out_err']
    config["fwb_file_name"] = ConfigSectionMap("Paths")['fwb_file_name']

    return config

