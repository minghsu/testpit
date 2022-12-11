#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from control.constant import STATE
import control.log as log
from datetime import datetime


class generate_report():
    def __init__(self):
        pass

    def execute(self, arg_model):

        end_time = datetime.today().strftime("%Y/%m/%d %H:%M:%S")
        log.info("")
        log.info("Finished time: '{}'".format(end_time))

        arg_model.report.endtime = end_time
        arg_model.report.report()

        return (STATE.EXIT, None)
