#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import os
from lxml import etree
from control.constant import DEF_CONFIG_FOLDER_NAME


class config:
    def __init__(self, arg_xmlconfig):
        self.__xml = None
        self.__project = None
        self.__description = None
        self.__report = None
        self.__devices = dict()
        self.__testcases = []
        xmlParser = etree.XMLParser(remove_blank_text=True)
        try:
            self.__xml = etree.parse(".{}{}{}{}".format(
                os.sep, DEF_CONFIG_FOLDER_NAME, os.sep, arg_xmlconfig), xmlParser)
            self.__load_info()
            self.__load_devices()
            self.__load_testcases()
        except Exception as e:
            self.__xml = None
            print(e)

    def __load_info(self):
        project_element = self.__xml.getroot().find("project")
        if project_element is not None:
            self.__project = project_element.text
        else:
            self.__project = "Project not define in xml config file"

        desc_element = self.__xml.getroot().find("description")
        if desc_element is not None:
            self.__description = desc_element.text
        else:
            self.__description = "Description not define in xml config file"

        report_element = self.__xml.getroot().find("report")
        if report_element is not None:
            self.__report = report_element.text
        else:
            self.__report = "standard"

    @property
    def project(self):
        return self.__project

    @property
    def description(self):
        return self.__description

    @property
    def report(self):
        return self.__report

    def __load_devices(self):
        devices_node = self.__xml.getroot().find("node").xpath("device")
        for device in devices_node:
            device_dict = dict()
            for element_node in device:
                if element_node.tag == "connect":
                    connect_dict = dict()
                    for connect_node in element_node:
                        connect_dict[connect_node.tag] = connect_node.text
                    device_dict[element_node.tag] = connect_dict
                elif element_node.tag == "command":
                    command_dict = dict()
                    for command_node in element_node:
                        if command_node.tag == "pre":
                            pre_command_list = []
                            for cmd in command_node:
                                pre_command_list.append(cmd.text)
                            command_dict['pre'] = pre_command_list
                        elif command_node.tag == "post":
                            post_command_list = []
                            for cmd in command_node:
                                post_command_list.append(cmd.text)
                            command_dict['post'] = post_command_list
                    device_dict[element_node.tag] = command_dict
                else:
                    device_dict[element_node.tag] = element_node.text
            self.__devices[device_dict['name']] = device_dict

    @property
    def devices(self):
        return self.__devices

    def __load_testcases(self):
        testcases_node = self.__xml.getroot().find("test").xpath("case")
        for case_node in testcases_node:
            testcase_dict = dict()
            for element_node in case_node:
                # to check the content type, translate tye data type at this section
                if element_node.get("type") == "int":
                    testcase_dict[element_node.tag] = int(element_node.text)
                else:
                    testcase_dict[element_node.tag] = element_node.text

            self.__testcases.append(testcase_dict)

    @property
    def testcases(self):
        return self.__testcases
