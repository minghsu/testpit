#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import os
import logging
from datetime import datetime
from control.output import output
from control.constant import DEF_LOG_FOLDER_NAME
from control.constant import DEF_SYSTEM_TAG


def init():
    logging.basicConfig(level=logging.DEBUG,
                        format='[%(name)10s] %(asctime)s %(levelname)-8s %(message)s',
                        datefmt='%m-%d %H:%M:%S',
                        handlers=[logging.FileHandler(datetime.today().strftime(DEF_LOG_FOLDER_NAME + os.sep + "%Y%m%d-%H%M%S.log"), 'w', 'utf-8'), ])


def info(arg_message, arg_log=True):
    if arg_log == True:
        logging.getLogger(DEF_SYSTEM_TAG).info(arg_message)

    output(arg_message)


def debug(arg_message, arg_log=True):
    if arg_log == True:
        logging.getLogger(DEF_SYSTEM_TAG).debug(arg_message)

    output(arg_message)


def error(arg_message, arg_log=True):
    if arg_log == True:
        logging.getLogger(DEF_SYSTEM_TAG).error(arg_message)

    output(arg_message, arg_color='red')


def critical(arg_message, arg_log=True):
    if arg_log == True:
        logging.getLogger(DEF_SYSTEM_TAG).critical(arg_message)

    output(arg_message, arg_color='red')
