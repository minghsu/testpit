#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import pexpect
from connect.base import base


class ssh(base):
    def __init__(self, arg_dev_name, arg_conn_conf):
        super().__init__(arg_dev_name, arg_conn_conf)

    def open(self):
        cmd = "ssh {}@{}".format(self.conn_conf['username'],
                                 self.conn_conf['hostname'])

        # prepare connect to ssh host
        if "port" in self.conn_conf:
            cmd = cmd + " -p {}".format(self.conn_conf['port'])

        self.spawn = pexpect.spawn(cmd, encoding='utf-8')
        try:
            result = self.spawn.expect(['password:', 'yes/no'],
                                       timeout=self.timeout)
            if result == 1:
                self.spawn.sendline("yes")
                result = self.spawn.expect(['password:'],
                                           timeout=self.timeout)
        except pexpect.EOF:
            raise Exception("Board is in use (connection refused).")

        self.spawn.sendline(self.conn_conf['password'])
        self.spawn.expect(self.prompt, timeout=self.timeout)

        return self.spawn

    def close(self):
        self.spawn.sendline("exit")
        self.spawn.expect(pexpect.EOF, timeout=self.timeout)

        # remove exist ssh key
        cmd = "ssh-keygen -R {}".format(self.conn_conf['hostname'])
        exit_spawn = pexpect.spawn(cmd)
        exit_spawn.expect(pexpect.EOF, timeout=self.timeout)
