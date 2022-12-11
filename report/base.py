#!/usr/bin/env python3
# -*- coding:utf-8 -*-

class base():
    def __init__(self):
        self.__result = []
        self.__project = None
        self.__description = None
        self.__starttime = None
        self.__endtime = None

    def add_result(self, arg_result):
        self.__result.append(arg_result)

    def get_all_results(self):
        return self.__result

    @property
    def project(self):
        return self.__project

    @project.setter
    def project(self, arg_project):
        self.__project = arg_project

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, arg_description):
        self.__description = arg_description

    @property
    def starttime(self):
        return self.__starttime

    @starttime.setter
    def starttime(self, arg_starttime):
        self.__starttime = arg_starttime

    @property
    def endtime(self):
        return self.__endtime

    @endtime.setter
    def endtime(self, arg_endtime):
        self.__endtime = arg_endtime
