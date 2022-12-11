#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import control.log as log
from control.constant import STATE


class close_device():
    def __init__(self):
        pass

    def execute(self, arg_model):
        devices = arg_model.get_devices()
        devices_config = arg_model.get_devices_config()
        log.info("")
        for device_key in devices:
            log.info("Closing '{}' device ...".format(
                devices_config[device_key]['name']))
            devices[device_key].close()

        return (STATE.GENERATE_REPORT, arg_model)
