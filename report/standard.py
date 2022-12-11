#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import os
import control.log as log
from datetime import datetime
from report.base import base
from control.constant import RESULT
from control.constant import DEF_TESTREPORT_FOLDER_NAME


class standard(base):
    def __init__(self):
        self.fileobject = None
        super().__init__()

    def report_output(self, arg_msg):
        log.info(arg_msg)
        self.fileobject.write(arg_msg + os.linesep)

    def report(self):
        width = 80

        report_time = datetime.today().strftime("%Y%m%d-%H%M%S")
        self.fileobject = open(
            ".{}{}{}REPORT_STANDARD_{}_{}.txt".format(os.sep, DEF_TESTREPORT_FOLDER_NAME, os.sep, self.project, report_time), "w")

        self.report_output("")
        self.report_output("-"*width)
        self.report_output("Project: {}".format(self.project))
        self.report_output("Description: {}".format(self.description))
        self.report_output("-"*width)
        self.report_output("Starting time: {}".format(self.starttime))
        self.report_output("")

        pass_count = 0
        fail_count = 0
        skip_count = 0
        unknown_count = 0
        all_results = self.get_all_results()
        total_count = len(all_results)
        for i in range(0, total_count):
            if all_results[i].result == RESULT.PASS:
                pass_count += 1
            elif all_results[i].result == RESULT.FAIL:
                fail_count += 1
            elif all_results[i].result == RESULT.SKIP:
                skip_count += 1
            else:
                unknown_count += 1

            if all_results[i].state != None:
                self.report_output("{:^3} - {:^10} - {:^20} - {}".format(i+1,
                                                                         all_results[i].result, all_results[i].state, all_results[i].desc))
            else:
                self.report_output("{:^3} - {:^10} - {:^20} - {}".format(i+1,
                                                                         all_results[i].result, "None", all_results[i].desc))

        self.report_output("Total tested case: {}, pass: {}, skip: {}, fail: {}, unknown: {}, pass rate: {}%".format(
            total_count, pass_count, skip_count, fail_count, unknown_count, (pass_count/total_count)*100))

        self.report_output("")
        self.report_output("Finished time: {}".format(self.endtime))
        self.report_output("-"*width)

        self.fileobject.close()
