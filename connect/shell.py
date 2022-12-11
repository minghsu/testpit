#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import pexpect
from connect.base import base


class shell(base):
    def __init__(self, arg_dev_name, arg_conn_conf):
        super().__init__(arg_dev_name, arg_conn_conf)

    def open(self):
        self.spawn = pexpect.spawn(
            self.conn_conf['shell'], encoding='utf-8')

        self.spawn.expect(self.prompt, timeout=self.timeout)
        return self.spawn

    def close(self):
        self.spawn.sendline("exit")
        self.spawn.expect(pexpect.EOF, timeout=self.timeout)
