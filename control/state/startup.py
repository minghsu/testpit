#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import os
import control.log as log
from control.constant import STATE
from control.constant import VERSION
from control.constant import DEF_LOG_FOLDER_NAME
from control.constant import DEF_TESTREPORT_FOLDER_NAME


class startup():
    def __init__(self):
        if not os.path.exists(DEF_LOG_FOLDER_NAME):
            os.makedirs(DEF_LOG_FOLDER_NAME)

        if not os.path.exists(DEF_TESTREPORT_FOLDER_NAME):
            os.makedirs(DEF_TESTREPORT_FOLDER_NAME)

    def execute(self, arg_model):
        width = 80

        log.info('*' * width)
        log.info('*' + (' ' * (width-2)) + '*')

        app_title = "{} Version: {}.{}.{}, ©Copyright 2022 Hsu Chih-Ming".format(
            VERSION.NAME,
            VERSION.MAJOR,
            VERSION.MINOR,
            VERSION.REVISION)

        reaming_space = width - len(app_title) - 2
        left_space = int(reaming_space/2)
        right_space = reaming_space - left_space

        log.info('*' + (' ' * left_space) +
                 app_title + (' ' * right_space) + '*')
        log.info('*' + (' ' * (width-2)) + '*')
        log.info('*' * width)

        return (STATE.LOAD_CONFIG, arg_model)
