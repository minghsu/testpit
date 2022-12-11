#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from ast import arg
import os
import importlib
from inspect import getmembers, isfunction
import control.log as log


class model:
    def __init__(self, arg_xmlconfig):
        self.__xmlconfig = arg_xmlconfig
        self.__config = None
        self.__report = None
        self.__devices = dict()
        self.__testcases = dict()

    @property
    def xmlconfig(self):
        return self.__xmlconfig

    @property
    def project(self):
        return self.__config.project

    @property
    def description(self):
        return self.__config.description

    @property
    def config(self):
        return self.__config

    @config.setter
    def config(self, arg_config):
        self.__config = arg_config

    @property
    def report(self):
        return self.__report

    @report.setter
    def report(self, arg_report):
        self.__report = arg_report

    def get_devices(self):
        return self.__devices

    def get_devices_config(self):
        return self.__config.devices

    def get_testcases(self):
        return self.__testcases

    def get_testcases_config(self):
        return self.__config.testcases

    def add_device(self, arg_name, arg_device):
        if arg_name is not None and arg_device is not None:
            self.__devices[arg_name] = arg_device

    def add_testcase(self, arg_name, arg_func):
        if arg_name is not None and arg_func is not None:
            self.__testcases[arg_name] = arg_func
