#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import abc
import logging

from control.logadapter import logadapter
from control.factory import connect


class base(abc.ABC):
    def __init__(self, arg_dev_conf):
        self.__dev_conf = arg_dev_conf
        self.__connect = connect(
            self.__dev_conf['name'],  self.__dev_conf['connect'])
        self.__pexpect = None

    def open(self):
        self.__pexpect = self.__connect.open()
        # logging

        if "color" in self.__dev_conf:
            self.__pexpect.logfile_read = logadapter(
                logging.getLogger(self.__dev_conf['name']), self.__dev_conf['color'])
        else:
            self.__pexpect.logfile_read = logadapter(
                logging.getLogger(self.__dev_conf['name']))

    def close(self):
        self.__pexpect.logfile_read = None
        self.__connect.close()

    def prompt(self):
        return self.__connect.prompt

    def sendline(self, arg_cmd):
        self.__pexpect.sendline(arg_cmd)

    def expect(self, arg_expect, arg_timeout=30):
        self.__pexpect.expect(arg_expect, timeout=arg_timeout)

    def before(self):
        if self.__pexpect is not None:
            return self.__pexpect.before

        return None

    def expect_prompt(self):
        self.__pexpect.expect(self.__connect.prompt,
                              timeout=self.__connect.timeout)

    def sendcontrol(self, arg_code):
        if self.__pexpect != None:
            self.__pexpect.sendcontrol(arg_code)
