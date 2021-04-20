#!/usr/bin/env pyhton
# -*- coding: utf-8 -*-
#
# Copyright (c) 2021 , Inc. All Rights Reserved
#

"""

Authors: jufei
Date: 2021/4/20 1:14 PM
"""


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        """
        从后向前遍历，如果一直是空格继续遍历，如果是字母，计数；计数后无论是遇到空格还是遍历结果，都返回当前计数结果；
        :param s:
        :return:
        """
        cur_len = 0
        for val in s[::-1]:
            if val == ' ':
                if cur_len > 0:
                    return cur_len
            else:
                cur_len += 1
        return cur_len
