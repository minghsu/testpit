#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import pexpect
from connect.base import base


class docker(base):
    def __init__(self, arg_dev_name, arg_conn_conf):
        super().__init__(arg_dev_name, arg_conn_conf)
        self.prompt.extend(['/ '])

    def open(self):
        # docker run --privileged --name docker1 -it ubuntu:latest
        cmd = "docker run --privileged --name {} -it {}".format(
            self.dev_name, self.conn_conf['image'])

        self.spawn = pexpect.spawn(cmd, encoding='utf-8')
        self.spawn.expect(self.prompt, timeout=self.timeout)

        return self.spawn

    def close(self):
        # exit docker session
        self.spawn.sendline("exit")
        self.spawn.expect(pexpect.EOF, timeout=self.timeout)

        # stop & remove old docker instance
        cmd = "docker stop {}".format(self.dev_name)
        exit_spawn = pexpect.spawn(cmd)
        exit_spawn.expect(pexpect.EOF, timeout=self.timeout)

        cmd = "docker rm {}".format(self.dev_name)
        exit_spawn = pexpect.spawn(cmd)
        exit_spawn.expect(pexpect.EOF, timeout=self.timeout)
        exit_spawn.close()
