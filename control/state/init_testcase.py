#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import os
import importlib

import control.log as log

from inspect import getmembers, isfunction
from control.constant import STATE


class init_testcase():
    def __init__(self):
        pass

    def execute(self, arg_model):
        testcase_list = os.listdir("./testcase")
        log.info("")
        for filename in testcase_list:
            name, ext = os.path.splitext(filename)
            if ext == ".py":
                try:
                    case_class = __import__(
                        "testcase.{}".format(name), fromlist=[name])

                    load_count = 0
                    for (case_name, case_func) in getmembers(case_class, isfunction):
                        arg_model.add_testcase(case_name, case_func)
                        load_count += 1

                    if load_count == 1:
                        log.info("Loaded '{}' testcase from file: {} ... ".format(load_count,
                                                                                  case_class.__file__))
                    else:
                        log.info("Loaded '{}' testcases from file: {} ... ".format(load_count,
                                                                                   case_class.__file__))

                except:
                    log.error("Error to import '%s' testcases." % (name))

        return (STATE.EXEC_PRE_CMD, arg_model)
