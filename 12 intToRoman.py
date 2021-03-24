#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2021 Baidu.com, Inc. All Rights Reserved
#

"""


Authors: jufei@baidu.com
Date:    2021/3/24
"""


class Solution:
    def intToRoman(self, num: int) -> str:
        """
        建立dict映射表，直接映射，可以多分几种情况讨论
        :param num:
        :return:
        """
        roman = ""
        val_roman = {
            5000: '', 1000: 'M', 500: 'D', 100: 'C', 50: 'L', 10: 'X', 5: 'V', 1: 'I'
            }
        for val in [1000, 100, 10, 1]:
            div, num = divmod(num, val)
            if div in [4, 9]:
                roman += val_roman[val]+val_roman[(div+1)*val]
            else:
                roman += val_roman[5*val]*(div//5) + val_roman[val]*(div%5)
        return roman