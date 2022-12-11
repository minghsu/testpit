#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# module
import control.log as log

# class
from control.constant import STATE
from control.factory import device


class init_device():
    def __init__(self):
        pass

    def execute(self, arg_model):
        # get all device xml config info
        devices_conf = arg_model.get_devices_config()

        # create device instance and add to 'model' class
        log.info("")
        for device_name in devices_conf.keys():
            arg_model.add_device(
                device_name, device(devices_conf[device_name]))
            log.info("Creating '{}' device, name is '{}' ...".format(
                devices_conf[device_name]['type'], device_name))

        return (STATE.OPEN_DEVICE, arg_model)
