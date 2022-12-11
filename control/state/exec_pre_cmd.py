#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import time
import control.log as log
from control.constant import STATE


class exec_pre_cmd():
    def __init__(self):
        pass

    def execute(self, arg_model):
        devices_config = arg_model.get_devices_config()
        devices = arg_model.get_devices()

        log.info("")
        for device_key in devices:
            for cmd in devices_config[device_key]['command']['pre']:
                log.info("[{}] Executing pre command: {}".format(
                    devices_config[device_key]['name'], cmd))
                devices[device_key].sendline(cmd)
                devices[device_key].expect_prompt()

        return (STATE.EXEC_TESTCASE, arg_model)
