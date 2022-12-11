#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# module
import control.log as log

# class
from control.constant import STATE


class open_device():
    def __init__(self):
        pass

    def execute(self, arg_model):
        devices = arg_model.get_devices()
        devices_config = arg_model.get_devices_config()

        log.info("")
        for device_key in devices:
            log.info("Opening '{}' device ...".format(
                devices_config[device_key]['name']))
            devices[device_key].open()

        return (STATE.INIT_TESTCASE, arg_model)
