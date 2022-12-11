#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import colorama
import os

'''
 for future use
'''

# style = {
#     'bright': colorama.Style.BRIGHT,
#     'dim': colorama.Style.DIM,
#     'normal': colorama.Style.NORMAL,
#     'reset_all': colorama.Style.RESET_ALL
# }

# color_back = {
#     'black': colorama.Back.BLACK,
#     'red': colorama.Back.RED,
#     'green': colorama.Back.GREEN,
#     'yellow': colorama.Back.YELLOW,
#     'blue': colorama.Back.BLUE,
#     'magenta': colorama.Back.MAGENTA,
#     'cyan': colorama.Back.CYAN,
#     'white': colorama.Back.WHITE,
#     'reset': colorama.Back.RESET
# }

color_fore = {
    'black': colorama.Fore.BLACK,
    'red': colorama.Fore.RED,
    'green': colorama.Fore.GREEN,
    'yellow': colorama.Fore.YELLOW,
    'blue': colorama.Fore.BLUE,
    'magenta': colorama.Fore.MAGENTA,
    'cyan': colorama.Fore.CYAN,
    'white': colorama.Fore.WHITE,
    'reset': colorama.Fore.RESET
}


def output(arg_str, arg_color=None):

    if arg_color != None and arg_color in color_fore:
        print("{}{}{}".format(color_fore[arg_color],
                              arg_str,
                              color_fore['reset']))
    else:
        print(arg_str)
