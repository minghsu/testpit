#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from control.statemachine import statemachine
from control.model import model


class controller:
    def __init__(self, arg_xmlconfig):
        self.__state = statemachine(model(arg_xmlconfig))

    def do_job(self):
        return self.__state.exec()
