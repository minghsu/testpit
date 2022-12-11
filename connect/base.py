#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import abc


class base(abc.ABC):
    def __init__(self, arg_dev_name, arg_conn_conf):
        self.spawn = None
        self.dev_name = arg_dev_name
        self.conn_conf = arg_conn_conf
        self.timeout = int(self.conn_conf['timeout'])

        '''
        $ matches the end of a line when parsed as a regex; it doesn't match a dollar sign. [$] should work; whether \$ does depends on what kind of string you put it in. 
        '''
        self.prompt = ['[$] ', '# ']
        # if "prompt" in self.conn_conf:
        #     self.prompt.extend(self.conn_conf['prompt'])

    @abc.abstractmethod
    def open(self):
        return NotImplemented

    @abc.abstractmethod
    def close(self):
        return NotImplemented
