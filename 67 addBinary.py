#!/usr/bin/env pyhton
# -*- coding: utf-8 -*-
#
# Copyright (c) 2021 , Inc. All Rights Reserved
#

"""

Authors: jufei
Date: 2021/4/22 1:38 PM
"""


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        """

        :param a:
        :param b:
        :return:
        """
        ans, add = '', 0
        index, a_len, b_len = -1, len(a), len(b)
        while max(a_len, b_len)+index >= 0 or add:
            if index + a_len >= 0:
                add += int(a[index])
            if index + b_len >= 0:
                add += int(b[index])
            add, cur = divmod(add, 2)
            ans = str(cur) + ans
            index += -1
        return ans
