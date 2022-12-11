#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# module
import sys
import colorama
import control.log as log

# class
#from control.config import config
from control.controller import controller

if __name__ == "__main__":
    log.init()
    colorama.init()
    # config = config()
    default_config = "default.xml"
    if len(sys.argv) >= 2:
        default_config = sys.argv[1]

    ctrl = controller(default_config)
    while (ctrl.do_job()):
        pass
