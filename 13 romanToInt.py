#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2021 Baidu.com, Inc. All Rights Reserved
#

"""


Authors: jufei@baidu.com
Date:    2021/3/30
"""


class Solution:
    def romanToInt(self, s: str) -> int:
        """
        建立好映射表，依次做映射加减即可；
        :param s:
        :return:
        """
        ret = 0
        char_int = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }
        for index, char in enumerate(s):
            if index < len(s)-1 and char_int[char] < char_int[s[index+1]]:
                ret -= char_int[char]
            else:
                ret += char_int[char]
        return ret