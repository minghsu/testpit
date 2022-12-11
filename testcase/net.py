#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import os
from unittest import result
from control.constant import RESULT


def ping(arg_device, arg_case, arg_result):

    # test case start
    result_check_patten = "received, "

    if arg_case['ipv6'] == "1":
        cmd = "ping -6 -c{} {}".format(arg_case['count'], arg_case['dest'])
    else:
        cmd = "ping -4 -c{} {}".format(arg_case['count'], arg_case['dest'])

    arg_device[arg_case['device']].sendline(cmd)
    arg_device[arg_case['device']].expect(
        ", time", arg_timeout=arg_case['timeout'])

    # result check
    result_msg = arg_device[arg_case['device']].before()
    start_pos = result_msg.find(result_check_patten)+len(result_check_patten)
    end_pos = result_msg[start_pos:].find(" ")

    arg_result.state = result_msg[start_pos:start_pos+end_pos] + " loss"

    if arg_result.state == "0% loss":
        arg_result.result = RESULT.PASS
    else:
        arg_result.result = RESULT.FAIL

    arg_device[arg_case['device']].expect_prompt()

    return arg_result


def iperf3(arg_device, arg_case, arg_result):

    server = arg_device[arg_case['server']]
    client = arg_device[arg_case['client']]

    server_addr = server.get_ipv4_addr()
    client_addr = client.get_ipv4_addr()

    server.sendline("iperf3 -s -D")
    server.expect_prompt()

    test_timer = 10
    if 'time' in arg_case:
        test_timer = arg_case['time']
    iperf3_cmd = "iperf3 -c {} -t {}".format(server_addr, test_timer)
    result_check_patten = "0.00-{}.00  sec   ".format(test_timer)

    # udp
    if arg_case['udp'] == "1":
        iperf3_cmd += " -u -b0"

    # reverse
    if arg_case['reverse'] == "1":
        iperf3_cmd += " -R"

    client.sendline(iperf3_cmd)
    client.expect("iperf Done.", arg_timeout=arg_case['timeout'])
    result_msg = client.before()
    arg_result.result = RESULT.PASS

    result_array = result_msg.split(os.linesep)
    sender_state = None
    receiver_state = None
    result_array_index = len(result_array)-1
    while ((sender_state == None or receiver_state == None) and result_array_index >= 0):
        receiver_pos = -1
        sender_pos = -1
        if (receiver_state == None):
            receiver_pos = result_array[result_array_index].find("receiver")

        if (sender_state == None):
            sender_pos = result_array[result_array_index].find("sender")

        if (receiver_pos >= 0 or sender_pos >= 0):
            column_array = result_array[result_array_index].split("  ")
            for column in column_array:
                if (column.find("/sec") >= 0):
                    if (receiver_pos >= 0):
                        receiver_state = column.strip().replace("/sec", "")
                    elif (sender_pos >= 0):
                        sender_state = column.strip().replace("/sec", "")
                    break

        result_array_index -= 1

    arg_result.state = "{}/{}".format(sender_state, receiver_state)

    client.expect_prompt()

    server.sendline("killall iperf3")
    server.expect_prompt()

    return arg_result
