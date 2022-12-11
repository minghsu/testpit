#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# module
import control.log as log

# class
from control.constant import STATE
from control.config import config
from control.factory import report
from datetime import datetime


class load_config():
    def __init__(self):
        pass

    def execute(self, arg_model):
        arg_model.config = config(arg_model.xmlconfig)
        arg_model.report = report(arg_model.config.report)

        log.info("Configuration: {}".format(arg_model.xmlconfig))
        log.info("Project: {}".format(arg_model.project))
        log.info("Description: {}".format(arg_model.description))
        start_time = datetime.today().strftime("%Y/%m/%d %H:%M:%S")
        log.info("Starting time: {}".format(start_time))

        arg_model.report.starttime = start_time
        arg_model.report.project = arg_model.project
        arg_model.report.description = arg_model.description

        return (STATE.INIT_DEVICE, arg_model)
