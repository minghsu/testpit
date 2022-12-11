#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from device.linux import linux


class android(linux):
    def __init__(self, arg_dev_conf):
        super().__init__(arg_dev_conf)
