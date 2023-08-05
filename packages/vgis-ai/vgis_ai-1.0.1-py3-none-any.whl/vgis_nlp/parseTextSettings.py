#!/usr/bin/python3.9
# -*- coding: utf-8 -*-
# @Time    : 2021/1/18 10:31
# @Author  : chenxw
# @Email   : gisfanmache.@gmail.com
# @File    : parseTextSettings.py
# @Descr   :
# @Software: PyCharm

class Setting:
    AIP_AUTH_STR = "323335353133363726262675506a66376f7a7a5947767a58327642523737506268515426262647444e6b6d68663444784853586749394d697841413662516932565777547257"
    AUTH_SPLIT_STR = "&&&"

    # 初始化
    def __init__(self):
        pass

    def get_AIP_AUTH_STR(self):
        return self.AIP_AUTH_STR

    def set_AIP_AUTH_STR(self, auth_str):
        self.AIP_AUTH_STR = auth_str

    def get_AUTH_SPLIT_STR(self):
        return self.AUTH_SPLIT_STR

    def set_AUTH_SPLIT_STR(self, split_str):
        self.AUTH_SPLIT_STR = split_str
