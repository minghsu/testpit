#!/usr/bin/env python3
# -*- coding:utf-8 -*-


import os
import sys
import traceback

from control.constant import STATE


class statemachine:
    def __init__(self, arg_model, arg_init_state=STATE.STARTUP):
        self.__state = arg_init_state
        self.__model = arg_model

    def exec(self):
        state_class = __import__("control.state.{}".format(
            self.__state), fromlist=[self.__state])
        state_instance = getattr(state_class, self.__state)()
        self.__state, self.__model = state_instance.execute(
            self.__model)

        if self.__state == STATE.NONE:
            return False

        return True
