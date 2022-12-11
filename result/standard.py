#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from control.constant import RESULT, RESULT_TYPE

# Type - Result - State - Description


class standard():
    def __init__(self, arg_type=RESULT_TYPE.NORMAL, arg_desc=""):
        self.type = arg_type
        self.result = RESULT.UNKNOWN
        self.desc = arg_desc
        self.state = None
