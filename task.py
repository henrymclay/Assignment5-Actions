"""
author: henry clay

date: 2/24/20

an automated testing assignment! file 1/2
"""

import math


def firstrun():
    return "success"


def circleArea(radius):
    pi = math.pi
    area = (pi * radius * radius)
    return area


def listFirstLast(input_list):
    return_list = []
    return_list.append(input_list[0])
    #return_list.reverse()
    return_list.append(input_list[-1])
    return return_list
