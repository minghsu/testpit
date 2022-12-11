#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from control.constant import STATE
import control.log as log
from datetime import datetime


class exit():
    def __init__(self):
        pass

    def execute(self, arg_model):
        return (STATE.NONE, None)
