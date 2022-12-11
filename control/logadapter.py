#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import os
import re
from control.output import output


class logadapter(object):
    def __init__(self, arg_logger, arg_color=None):
        self.logger = arg_logger
        self.color = arg_color

    def write(self, arg_data):
        ESC = r'\x1b'
        CSI = ESC + r'\['
        OSC = ESC + r'\]'
        CMD = '[@-~]'
        ST = ESC + r'\\'
        BEL = r'\x07'
        pattern = '(' + CSI + '.*?' + CMD + '|' + OSC + \
            '.*?' + '(' + ST + '|' + BEL + ')' + ')'

        # NOTE: data can be a partial line, multiple lines
        data = arg_data.strip()  # ignore leading/trailing whitespace

        if data:  # non-blank
            lst_string = data.split(os.linesep)
            for str in lst_string:
                self.logger.info(re.sub(pattern, '', str))
                output(str, arg_color=self.color)

    def flush(self):
        pass  # leave it to logging to flush properly
