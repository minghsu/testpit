#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import os
import importlib
import control.log as log
from result import standard as standard_result
from report import standard as standard_report


def device(arg_dev_conf):
    device_list = os.listdir("./device")
    for filename in device_list:
        name, ext = os.path.splitext(filename)
        if ext == ".py" and name == arg_dev_conf['type']:
            try:
                device_class = __import__(
                    "device.{}".format(name), fromlist=[name])
                return getattr(device_class, name)(arg_dev_conf)
            except:
                log.error("Error to import '%s' device." % (name))

    return None


def connect(arg_dev_name, arg_conn_conf):
    connect_list = os.listdir("./connect")
    for filename in connect_list:
        name, ext = os.path.splitext(filename)
        if ext == ".py" and name == arg_conn_conf['type']:
            try:
                connect_class = __import__(
                    "connect.{}".format(name), fromlist=[name])
                return getattr(connect_class, name)(arg_dev_name, arg_conn_conf)
            except:
                log.error("Error to import '%s' connect." % (name))

    return None


def result(arg_case_conf):
    result_type = None
    if 'result' in arg_case_conf:
        result_type = arg_case_conf['result']
    else:
        result_type = 'standard'

    result_list = os.listdir("./result")
    for filename in result_list:
        name, ext = os.path.splitext(filename)
        if ext == ".py" and name == result_type:
            try:
                connect_class = __import__(
                    "result.{}".format(name), fromlist=[name])
                return getattr(connect_class, name)(arg_desc=arg_case_conf['description'])
            except:
                log.error("Error to import '%s' result class." % (name))

    return standard_result(arg_desc=arg_case_conf['description'])


def report(arg_report_name):

    report_list = os.listdir("./report")
    for filename in report_list:
        name, ext = os.path.splitext(filename)
        if ext == ".py" and name == arg_report_name:
            try:
                connect_class = __import__(
                    "report.{}".format(name), fromlist=[name])
                return getattr(connect_class, name)()
            except:
                log.error("Error to import '%s' report class." % (name))

    return standard_report()
