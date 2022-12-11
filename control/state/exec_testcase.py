#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import control.log as log
from control.constant import STATE
from control.constant import RESULT
from control.factory import result


class exec_testcase():
    def __init__(self):
        pass

    def execute(self, arg_model):
        run_testcases = arg_model.config.testcases
        loaded_testcases = arg_model.get_testcases()
        exec_devices = arg_model.get_devices()

        log.info("")
        for run_case in run_testcases:
            if run_case['name'] in loaded_testcases.keys():
                run_result = None
                if "skip" in run_case and run_case['skip'] == "1":
                    log.info("Skipping '{}' case: {}".format(
                        run_case['name'], run_case['description']))
                    run_result = result(run_case)
                    run_result.result = RESULT.SKIP
                    run_result.state = "N/A"
                else:
                    log.info("Executing '{}' case: {}".format(
                        run_case['name'], run_case['description']))
                    run_result = loaded_testcases[run_case['name']](
                        exec_devices, run_case, result(run_case))

                arg_model.report.add_result(run_result)

                log.info("The '{}' case tested result is '{}'".format(
                    run_case['name'], run_result.result))

                log.info("")

        return (STATE.EXEC_POST_CMD, arg_model)
