#!/usr/bin/env python3
# -*- coding:utf-8 -*-

DEF_SYSTEM_TAG = "system"
DEF_LOG_FOLDER_NAME = "logs"
DEF_CONFIG_FOLDER_NAME = "config"
DEF_TESTREPORT_FOLDER_NAME = "testreports"


class VERSION:
    NAME = "Test Pit"
    MAJOR = "0"
    MINOR = "0"
    REVISION = "1"


class STATE:
    NONE = 'none'
    STARTUP = 'startup'
    EXIT = 'exit'
    LOAD_CONFIG = 'load_config'
    INIT_DEVICE = 'init_device'
    OPEN_DEVICE = 'open_device'
    CLOSE_DEVICE = 'close_device'
    INIT_TESTCASE = "init_testcase"
    EXEC_TESTCASE = "exec_testcase"
    EXEC_PRE_CMD = "exec_pre_cmd"
    EXEC_POST_CMD = "exec_post_cmd"
    GENERATE_REPORT = "generate_report"


class RESULT_TYPE:
    NORMAL = "normal"


class RESULT:
    UNKNOWN = "UNKNOWN"
    SKIP = "SKIP"
    PASS = "PASS"
    FAIL = "FAIL"
