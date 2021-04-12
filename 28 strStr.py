#!/usr/bin/env pyhton
# -*- coding: utf-8 -*-
#
# Copyright (c) 2021 , Inc. All Rights Reserved
#

"""

Authors: jufei
Date: 2021/4/7 4:48 PM
"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        """
        依次匹配
        :param haystack:
        :param needle:
        :return:
        """
        len_n = len(needle)
        for i in range(len(haystack)-len(needle)+1):
            j = 0
            while j < len_n and haystack[i+j] == needle[j]:
                j += 1
            if j == len_n:
                return i
        return -1
