#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import os
import netifaces
from device.base import base


class linux(base):
    def __init__(self, arg_dev_conf):
        super().__init__(arg_dev_conf)

    @property
    def kernel_release(self):
        self.sendline("uname -r")
        self.expect_prompt()
        result_msg = self.before().split(os.linesep)
        return result_msg[1]

    def get_ipv4_addr(self, arg_if="eth0"):
        return netifaces.ifaddresses(arg_if)[netifaces.AF_INET][0]['addr']
