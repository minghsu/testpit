#!/usr/bin/env python3
# -*- coding:utf-8 -*-

def meminfo(arg_device, arg_case, arg_result):

    arg_device[arg_case['device']].sendline("free")
    arg_device[arg_case['device']].expect_prompt()

    return arg_result
